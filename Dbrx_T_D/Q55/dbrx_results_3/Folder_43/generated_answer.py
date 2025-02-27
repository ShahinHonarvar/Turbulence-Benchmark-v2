from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for sub_array in circular_sublists(lst):
        if product(sub_array) == n:
            result.append(sub_array)
    return result

def product(num_list):
    return reduce(lambda x, y: x * y, num_list, 1)

def circular_sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]