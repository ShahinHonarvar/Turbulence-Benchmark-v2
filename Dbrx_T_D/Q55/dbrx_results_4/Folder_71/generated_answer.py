from itertools import islice

def circular_list_product(circular_list, sublist_size):
    product = 1
    for _ in range(sublist_size):
        product *= circular_list[0]
        circular_list = circular_list[1:] + circular_list[:1]
    return product

def sublists_with_product_equal_n(circular_list, n):
    result = []
    for sublist_size in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            sublist = islice(circular_list, i, i + sublist_size)
            if circular_list_product(sublist, sublist_size) == n:
                result.append(list(sublist))
    return result