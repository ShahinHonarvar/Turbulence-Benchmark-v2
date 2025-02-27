def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left = 0
        current_product = 1
        result = []
        for right in range(length):
            current_product *= arr[right]
            while current_product % target_product == 0:
                if current_product == target_product:
                    result.append(arr[left:right + 1])
                current_product //= arr[left]
                left += 1
        return result
    target_product = -690
    unique_list = list(set(circular_list))
    unique_list.sort()
    all_subarrays = []
    for i in range(len(unique_list)):
        subarrays = find_subarrays(unique_list[i:], target_product)
        for subarray in subarrays:
            all_subarrays.append(subarray)
    return all_subarrays