def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left = 0
        current_product = 1
        result = []
        for right in range(length):
            current_product *= arr[right]
            while current_product != 0 and current_product % target_product == 0:
                result.append(arr[left:right + 1])
                current_product = current_product // target_product
                left += 1
        return result
    subarrays = find_subarrays(circular_list, -690)
    unique_subarrays = [tuple(sub) for sub in set(map(tuple, subarrays))]
    unique_subarrays.sort(key=lambda x: x[0])
    return [list(sub) for sub in unique_subarrays]