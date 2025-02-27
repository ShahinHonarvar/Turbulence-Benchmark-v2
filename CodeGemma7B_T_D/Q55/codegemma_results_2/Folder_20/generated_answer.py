from itertools import count
from functools import reduce
from operator import mul

def circular_list_prod(circular_list):
    for i in count():
        circular_list.append(circular_list.pop(0))
        if len(circular_list) > i:
            break

def func(lists, product, circular_list):
    i = 0
    while i < len(circular_list):
        if reduce(mul, circular_list[i:i + product]) == -69:
            lists.append(circular_list[i:i + product])
        i += 1

def lists_with_product_equal_n(circular_list):
    lists = []
    product = len(circular_list)
    while product > 0:
        circular_list_prod(circular_list)
        func(lists, product, circular_list)
        circular_list.append(circular_list.pop(0))
        product -= 1
    return lists