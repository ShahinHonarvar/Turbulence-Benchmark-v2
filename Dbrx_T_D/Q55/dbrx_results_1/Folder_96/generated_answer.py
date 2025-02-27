from itertools import islice

def is_circular_sublist_equal_to_n(subelements, n):
    if len(subelements) == 0:
        return n == 1
    if n % subelements[0] == 0:
        return is_circular_sublist_equal_to_n(subelements[1:], n // subelements[0])
    return is_circular_sublist_equal_to_n(subelements[1:], n)

def circular_list_product(circular_list):
    product = 1
    for elem in circular_list:
        product *= elem
    return product

def lists_with_product_equal_n(circular_list):
    n = circular_list_product(circular_list)
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            subelements = circular_list[i:j + 1]
            if is_circular_sublist_equal_to_n(subelements, n):
                result.append(subelements)
    return result