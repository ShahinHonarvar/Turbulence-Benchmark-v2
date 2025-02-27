from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    n = -94
    result = []
    size = len(circular_list)
    circular_list += circular_list
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end + 1])
    return result