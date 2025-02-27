from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def product(lst: List[int]) -> int:
        result = 1
        for num in lst:
            result *= num
        return result
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product(sublist) == 632 and len(sublist) <= len(circular_list):
                result.append(sublist)
    return result