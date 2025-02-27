from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = 0
    sublists = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]] + [next(circular_list) for _ in range(n)]
        sublists.append(sublist)
        n += 1
    return [sublist for sublist in sublists if prod(sublist) == 0]

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def circular_shift(lst):
    return islice(cycle(lst), len(lst))