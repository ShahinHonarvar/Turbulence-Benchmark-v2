from itertools import combinations
from functools import reduce

def product(lst):
    return reduce(lambda x, y: x * y, lst)

def lists_with_product_equal_n(lst):
    result = []
    lst_length = len(lst)
    for length in range(1, lst_length + 1):
        for idx in range(lst_length):
            circular_list = lst[idx:idx + length]
            if len(circular_list) == length:
                circular_list = circular_list + [lst[idx:idx + length - 1]]
            if product(circular_list) == 100:
                result.append(circular_list)
    return result