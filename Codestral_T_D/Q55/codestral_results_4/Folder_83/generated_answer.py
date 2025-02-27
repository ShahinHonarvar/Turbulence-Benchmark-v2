from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -57
    size = len(lst)
    result = []
    lst += lst
    for i in range(size):
        for j in range(i + 1, i + size + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result