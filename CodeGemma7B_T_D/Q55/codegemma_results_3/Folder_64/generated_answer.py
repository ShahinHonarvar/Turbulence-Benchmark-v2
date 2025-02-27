from itertools import product
import math

def lists_with_product_equal_n(lst):
    circular = lst + [lst[0]]
    prod = lst[0]
    lists = []
    for start in range(len(circular)):
        for end in range(1, len(circular)):
            if end - start + 1 > len(lst):
                continue
            if prod * circular[end] / circular[start] == math.prod(circular[start + 1:end + 1]):
                lists.append(circular[start + 1:end + 1])
            prod *= circular[end]
    return lists