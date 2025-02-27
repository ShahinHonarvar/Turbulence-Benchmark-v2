from itertools import islice

def lists_with_product_equal_n(circular_list):
    circular_list_size = len(circular_list)
    sublists_of_size_i = [circular_list[i // circular_list_size:] + circular_list[:i // circular_list_size] for i in range(circular_list_size)]
    sublists_with_product_equal_n = [sublist for sublist in sublists_of_size_i if product(sublist) == -938]
    return sublists_with_product_equal_n

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result