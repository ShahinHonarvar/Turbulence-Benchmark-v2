from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:
    result = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        current_sublist = [circular_list[i]]
        for j in range((i + 1) % len(circular_list), i + len(circular_list), (i + 1) % len(circular_list)):
            product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if product == -65:
                result.append(current_sublist[:])
    return result