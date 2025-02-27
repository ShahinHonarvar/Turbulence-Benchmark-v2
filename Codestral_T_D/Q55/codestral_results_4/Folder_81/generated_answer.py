from typing import List
from itertools import cycle, islice

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    n = -8
    result = []
    for start in range(len(circular_list)):
        product = 1
        temp = []
        for num in islice(cycle(circular_list), start, start + len(circular_list)):
            product *= num
            temp.append(num)
            if product == n:
                result.append(temp.copy())
            if product != 0 and n % product != 0:
                break
    return result