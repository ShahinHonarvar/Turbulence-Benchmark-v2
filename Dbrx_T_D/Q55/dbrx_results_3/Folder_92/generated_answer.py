from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_contiguous(sublist):
        for i in range(len(sublist) - 1):
            if sublist[i] * sublist[i + 1] > 5:
                return False
        return True
    sublists = []
    visited = set()
    for i in range(len(circular_list)):
        if (i, circular_list[i]) not in visited:
            visited.add((i, circular_list[i]))
            for j in range(i + 1, len(circular_list)):
                if (j, circular_list[j]) not in visited:
                    visited.add((j, circular_list[j]))
                    sublist = [circular_list[i], circular_list[j]]
                    if 5 in sublist:
                        sublists.append(sublist)
                    elif is_contiguous(sublist):
                        sublists.append(sublist)
                        for k in range(j + 1, len(circular_list)):
                            if (k, circular_list[k]) not in visited:
                                visited.add((k, circular_list[k]))
                                sublist.append(circular_list[k])
                                if 5 in sublist:
                                    sublists.append(sublist)
                                elif is_contiguous(sublist):
                                    sublists.append(sublist)
                                sublist.pop()
                                visited.remove((k, circular_list[k]))
    for i in combinations(circular_list, 2):
        if (i, 1) not in visited:
            visited.add((i, 1))
            sublist = [x for x in i]
            if 5 in sublist:
                sublists.append(sublist)
            elif is_contiguous(sublist):
                sublists.append(sublist)
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if (j, 1) not in visited:
                visited.add((j, 1))
                sublist = [x for x in j]
                if 5 in sublist:
                    sublists.append(sublist)
                elif is_contiguous(sublist):
                    sublists.append(sublist)
    return sublists