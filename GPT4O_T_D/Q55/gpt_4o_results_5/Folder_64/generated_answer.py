from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    circular_list_extended = circular_list + circular_list[:-1]
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = circular_list_extended[start:start + size]
            if product(sublist) == 3:
                result.append(sublist)
    return result