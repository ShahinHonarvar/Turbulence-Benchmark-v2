from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(array, target, n):
        result = []
        for i in range(len(array)):
            product = 1
            subarray = []
            for j in range(i, min(i + n, len(array))):
                product *= array[j]
                subarray.append(array[j])
                if product == target:
                    result.append(subarray)
        return result
    sublists = find_subarrays(circular_list, 33, len(circular_list))
    return sublists