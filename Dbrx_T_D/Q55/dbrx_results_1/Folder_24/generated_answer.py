from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -89
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list[i % len(circular_list):]), len(circular_list)))
        if sublists_with_product_equal_n(sublist, n):
            result.append(sublist)
    return result

def sublists_with_product_equal_n(sublist, n):
    if not sublist:
        return n == 1
    if multiply_list(sublist) == n:
        return True
    return sublists_with_product_equal_n(sublist[1:], n)

def multiply_list(sublist):
    result = 1
    for num in sublist:
        result *= num
    return result