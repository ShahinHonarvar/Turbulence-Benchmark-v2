from itertools import islice

def sublists_with_product_equal_n(lst, n=53):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = list(islice(circular(lst), j - i + 1))
            if prod(sublist) == n:
                result.append(sublist)
    return result

def circular(lst):
    while True:
        yield from lst
        lst = lst[1:] + lst[:1]

def prod(lst):
    res = 1
    for num in lst:
        res *= num
    return res