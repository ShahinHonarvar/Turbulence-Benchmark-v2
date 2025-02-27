from itertools import combinations

def lists_with_product_equal_n(lst):
    n = 15
    result = []
    size = len(lst)
    lst = lst + lst
    for i in range(size):
        for j in range(1, size + 1):
            if j > i:
                sublist = lst[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result