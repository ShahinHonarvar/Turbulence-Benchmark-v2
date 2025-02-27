from itertools import product

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for r in range(2, n + 1):
        for i in range(n - r + 2):
            sublist = lst[i:i + r]
            if sublist != sublist[::-1]:
                product = 1
                for num in sublist:
                    product *= num
                if product == -94:
                    result.append(sublist)
    return result