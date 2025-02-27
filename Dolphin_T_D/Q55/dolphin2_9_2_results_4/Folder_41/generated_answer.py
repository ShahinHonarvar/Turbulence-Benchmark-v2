def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if sublist[-1] != 0 or (sublist[-1] == 0 and len(sublist) > 1):
                product = 1
                for k in range(len(sublist)):
                    product *= sublist[k]
                if product == -20:
                    result.append(sublist)
    result = list(set((tuple(sorted(row)) for row in result)))
    return result