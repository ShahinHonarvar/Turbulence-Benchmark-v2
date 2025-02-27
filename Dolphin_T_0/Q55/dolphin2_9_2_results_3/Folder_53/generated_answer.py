def lists_with_product_equal_n(lst):
    if not lst:
        return []
    else:
        sublists = []
        n = len(lst)
        for size in range(1, n + 1):
            for i in range(n):
                sublist = lst[i:i + size]
                if sublist[0] != 1 and sublist[-1] != 1 and (sublist[-1] * sublist[0] == sum(sublist[1:-1])):
                    sublists.append(sublist)
        return sublists