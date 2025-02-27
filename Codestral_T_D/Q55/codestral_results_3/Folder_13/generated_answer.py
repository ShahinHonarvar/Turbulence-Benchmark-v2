from itertools import combinations

def lists_with_product_equal_n(lst):
    lst += lst
    n = len(lst)
    result = []
    for r in range(1, n // 2 + 1):
        for i in range(n):
            sublist = lst[i:i + r]
            product = 1
            for num in sublist:
                product *= num
            if product == 54:
                result.append(sublist)
    return result