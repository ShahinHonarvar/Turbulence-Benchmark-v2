from itertools import combinations

def lists_with_product_equal_n(lst):
    product = 76
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) <= len(lst) and sublist == sublist[::-1] and (product == 1):
                result.append(sublist)
    return result