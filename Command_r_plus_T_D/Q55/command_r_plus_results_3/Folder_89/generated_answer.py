from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    result = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == 57:
            result.append(circular_list[i - len(circular_list):i + 1])
            product = 1
    return result