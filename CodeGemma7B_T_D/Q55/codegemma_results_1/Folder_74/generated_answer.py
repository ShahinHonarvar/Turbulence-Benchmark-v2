from itertools import product, combinations

def lists_with_product_equal_n(circular_list):

    def multiply(elem):
        total = 1
        for item in elem:
            total *= item
        return total

    def check_circular(circular_list):
        size = len(circular_list)
        for i in range(size):
            for j in range(i + 2, size + 1):
                yield circular_list[i:j]
    for length in range(1, len(circular_list) + 1):
        for sublist in combinations(check_circular(circular_list), length):
            if multiply(sublist) == 51:
                return [list(elem) for elem in sublist]
    return []