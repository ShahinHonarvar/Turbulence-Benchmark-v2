from itertools import islice

def circular_sublists(lst):
    return lst + lst[:1]

def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

def lists_with_product_equal_n(lst, n=4):
    result = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst) - i + 1):
            sublist = circular_sublists(islice(lst, j, j + i))
            if product(sublist) == n:
                result.append(list(sublist))
    return result