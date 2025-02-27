from itertools import combinations_with_replacement
from math import prod

def lists_with_product_equal_n(circular_list):
    radius = len(circular_list) + 1
    result = []
    for offset in range(radius):
        for size in range(1, radius - offset):
            for sublist in combinations_with_replacement(circular_list, size):
                sequence = sublist * 2 + circular_list[:offset]
                sequence = sequence[offset:offset + size]
                if prod(sequence) == 45:
                    result.append(list(sequence))
    return result