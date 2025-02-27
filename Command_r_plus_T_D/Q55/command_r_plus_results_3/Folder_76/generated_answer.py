from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(lst, target, size):
        result = []
        for i in range(len(lst)):
            for j in range(i, min(i + size, len(lst))):
                if product(lst[i:j + 1]) == target:
                    result.append(lst[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    target_product = 247
    max_size = len(circular_list)
    all_subarrays = []
    for size in range(1, max_size + 1):
        subarrays = find_subarrays(circular_list, target_product, size)
        all_subarrays.extend(subarrays)
    return all_subarrays