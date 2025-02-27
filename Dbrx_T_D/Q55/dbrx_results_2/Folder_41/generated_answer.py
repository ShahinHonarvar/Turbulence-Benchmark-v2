from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    n = -20

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    for i in range(1, len(circular_list) + 1):
        combs = combinations(circular_list, i)
        for comb in combs:
            if product_of_list(comb) == n:
                result.append(list(comb))
    return result