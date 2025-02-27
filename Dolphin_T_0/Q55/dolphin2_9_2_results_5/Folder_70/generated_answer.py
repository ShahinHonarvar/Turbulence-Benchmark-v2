def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if sublist[-1] == sublist[0]:
                continue
            elif sublist[-1] * sublist[0] == 32:
                for item in sublist:
                    product *= item
            if product == 32:
                result.append(sublist)
    return result