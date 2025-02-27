from itertools import cycle, islice
from math import prod
from typing import List

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = list(islice(cycle(lst), start, end))
            if prod(sublist) == 0:
                result.append(sublist)
    return result