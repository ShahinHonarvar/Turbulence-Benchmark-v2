from collections import deque

def lists_with_product_equal_n(lst):
    sublists = []
    circular_lst = lst + lst[::-1]
    for length in range(1, len(lst) + 1):
        for start in range(len(lst)):
            end = start + length
            if prod(circular_lst[start:end]) == 74:
                sublists.append(circular_lst[start:end])
    return sublists

def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product