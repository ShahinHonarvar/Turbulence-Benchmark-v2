def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left = 0
        curr_product = 1
        result = []
        for right in range(length):
            curr_product *= arr[right]
            while curr_product == target_product or (curr_product > target_product and left < right):
                result.append(arr[left:right + 1])
                curr_product /= arr[left]
                left += 1
        return result
    target_product = -6
    unique_sublists = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], target_product)
        unique_sublists.extend(subarrays)
    return unique_sublists