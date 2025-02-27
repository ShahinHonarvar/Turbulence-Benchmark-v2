from itertools import combinations_with_replacement, product, permutations

def lists_with_product_equal_n(circlist, n=-69):
    lists = []
    for i in range(len(circlist)):
        circlist.append(circlist.pop(0))
        temp_lists = []
        for j in range(i + 1, len(circlist)):
            thislist = [circlist[x] for x in range(j, j + i + 1)]
            if len(thislist) <= len(circlist) and len(thislist) >= 0 and (product(thislist) == (-69,)):
                temp_lists.append(thislist)
        lists.extend(temp_lists)
    return lists