def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left = 0
        curr_product = 1
        for right in range(length):
            curr_product *= arr[right]
            while curr_product == target_product or (right - left + 1 > length or curr_product * arr[left] < target_product):
                if curr_product == target_product:
                    yield arr[left:right + 1]
                left += 1
                curr_product //= arr[left - 1]
    target_product = -44
    unique_subarrays = []
    for subarray in find_subarrays(circular_list, target_product):
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays