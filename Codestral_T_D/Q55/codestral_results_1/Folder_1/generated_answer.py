from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -51
    lst *= 2
    for i in range(1, len(lst) // 2 + 1):
        for j in range(len(lst) // 2):
            sublst = lst[j:j + i]
            product = 1
            for num in sublst:
                product *= num
            if product == n:
                yield sublst