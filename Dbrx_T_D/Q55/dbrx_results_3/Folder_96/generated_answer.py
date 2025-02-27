from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 0
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if n != 0 and prod(sublist) == n or prod(sublist) == 0:
            result.append(sublist)
        if prod(sublist) == n:
            break
    return result

def prod(iterable):
    return reduce(lambda x, y: x * y, iterable, 1)