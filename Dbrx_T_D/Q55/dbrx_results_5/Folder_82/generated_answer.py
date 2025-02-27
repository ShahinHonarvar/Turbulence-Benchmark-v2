from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 8
    result = []
    for i in range(len(circular_list)):
        sub_result = []
        for j in range(1, len(circular_list)):
            sub_result.append(circular_list[i:j])
            if prod(sub_result) == n:
                result.append(sub_result)
        i += 1
    return result

def prod(sub_result):
    product = 1
    for i in sub_result:
        product *= i
    return product

def get_circular_list(list):
    return list + [list[0]]