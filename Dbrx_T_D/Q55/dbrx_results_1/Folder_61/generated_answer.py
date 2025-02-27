from itertools import islice

def circular_sublists(lst):
    return (lst[i:] + lst[:i] for i in range(len(lst)))

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)

def lists_with_product_equal_n(lst, n):
    result = []
    for sublist in circular_sublists(lst):
        for i in range(1, len(sublist) + 1):
            if product(sublist[:i]) == n:
                result.append(sublist[:i])
    return result