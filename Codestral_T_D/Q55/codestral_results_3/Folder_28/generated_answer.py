from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    n = 85
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j + 1])
    return result