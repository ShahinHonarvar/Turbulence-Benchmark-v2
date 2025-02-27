from itertools import islice, product

def circular_list_product(lst, n, start=0):
    for i in range(start, len(lst)):
        if lst[i] == n:
            yield lst[start:i + 1]
        elif lst[i] < 0 < n:
            break

def iterative_circular_sublists(lst):
    while lst:
        yield lst
        lst = lst[1:] + lst[:1]

def is_product_equal_n(sublist, n=33):
    return reduce(lambda x, y: x * y, sublist, 1) == n

def lists_with_product_equal_n(lst):
    circular_sublists = list(iterative_circular_sublists(lst))
    result = []
    for circular_sublist in circular_sublists:
        for sublist in product(circular_sublist, repeat=len(circular_sublist)):
            if is_product_equal_n(sublist):
                result.append(list(sublist))
    return result