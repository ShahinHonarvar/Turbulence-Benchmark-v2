from itertools import combinations

def lists_with_product_equal_n(lst):
    n = 27
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + r] + lst[:(i + r) % len(lst)]
            product = 1
            for num in sublist:
                product *= num
                if product > n:
                    break
            if product == n:
                result.append(sublist)
    return result