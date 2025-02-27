from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = 42
    length = len(circular_list)
    results = []

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    for start in range(length):
        for end in range(1, length + 1):
            indices = [(start + i) % length for i in range(end)]
            sublist = [circular_list[i] for i in indices]
            if product(sublist) == n:
                results.append(sublist)
    return results