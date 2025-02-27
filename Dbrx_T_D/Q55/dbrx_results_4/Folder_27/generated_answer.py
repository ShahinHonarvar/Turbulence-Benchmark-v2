from itertools import islice, combinations

def lists_with_product_equal_n(lst, n=-82):
    result = []
    for length in range(1, len(lst) + 1):
        for i in range(len(lst) - length + 1):
            sublst = list(islice(circular_iter(lst, i), length))
            if product(sublst) == n:
                result.append(sublst)
    return result

def circular_iter(lst, start):
    while True:
        yield lst[start]
        start = (start + 1) % len(lst)

def product(iterable):
    p = 1
    for num in iterable:
        p *= num
    return p