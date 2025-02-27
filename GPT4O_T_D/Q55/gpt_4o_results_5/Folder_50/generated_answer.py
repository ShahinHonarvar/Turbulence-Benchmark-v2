from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for r in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(r)]
            if product(sublist) == 45:
                result.append(sublist)
    return result