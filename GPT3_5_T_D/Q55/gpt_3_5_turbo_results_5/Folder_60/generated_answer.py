from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(1, size + 1):
        for combo in combinations(lst, i):
            product = 1
            for num in combo:
                product *= num
            if product == 49:
                result.append(list(combo))
    return result