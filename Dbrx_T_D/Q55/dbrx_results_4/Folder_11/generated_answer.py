from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -15
    sublists = []
    for i in range(len(circular_list)):
        window = list(islice(cycle(circular_list), i, i + len(circular_list)))
        for j in range(len(window)):
            sublist = window[j:j + n]
            if len(sublist) < 2:
                continue
            if prod(sublist) == n:
                sublists.append(sublist)
    return sublists

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result