import itertools

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(itertools.permutations(circular_list, i))
    result = [sublist for sublist in sublists if product(sublist) == -97]
    return result

def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total