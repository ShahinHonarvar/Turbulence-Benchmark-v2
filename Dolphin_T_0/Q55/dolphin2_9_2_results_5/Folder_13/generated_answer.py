def list_product(lst):
    product = 1
    for i in lst:
        product *= i
    return product

def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    if length == 0:
        return result
    for start_index in range(length):
        for end_index in range(start_index + 1, length + 1):
            product = list_product(lst[start_index:end_index])
            if product == 54:
                result.append(lst[start_index:end_index])
    return result