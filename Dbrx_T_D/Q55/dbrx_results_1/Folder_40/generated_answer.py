from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            sublist = list(j)
            if sublist[0] == -9 and -9 not in sublist[1:]:
                sublists.append(sublist)
            elif sublist[0] != -9 and product(sublist) == -9:
                sublists.append(sublist)
    return sublists

def product(sublist):
    if len(sublist) == 1:
        return sublist[0]
    else:
        return sublist[0] * product(sublist[1:])