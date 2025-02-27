from itertools import islice

def lists_with_product_equal_n(circular_list):
    list_size = len(circular_list)
    for i in range(list_size):
        sublist = list(islice(circular_list, i, i + list_size))
        product = 1
        for element in sublist:
            product *= element
        if product == -30:
            return sublist
    return []