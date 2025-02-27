from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left, right = (0, 0)
        current_product = 1
        result = []
        for right in range(length):
            current_product *= arr[right]
            while current_product > 0 and current_product % target_product == 0:
                result.append(arr[left:right + 1])
                current_product /= target_product
                left += 1
        return result
    target_product = 48
    subarrays = find_subarrays(circular_list, target_product)
    subarrays.extend(find_subarrays(circular_list[::-1], target_product))
    unique_subarrays = []
    for subarray in subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays