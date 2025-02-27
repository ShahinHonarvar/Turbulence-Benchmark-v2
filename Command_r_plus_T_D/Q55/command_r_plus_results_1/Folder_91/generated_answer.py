def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target):
        length = len(arr)
        left = 0
        curr_product = 1
        result = []
        for right in range(length):
            curr_product *= arr[right]
            while curr_product > 0 and curr_product % target == 0:
                result.append(arr[left:right + 1])
                curr_product /= arr[left]
                left += 1
        return result
    subarrays = find_subarrays(circular_list, 2)
    unique_subarrays = [tuple(sub) for sub in set(map(tuple, subarrays))]
    result = [list(sub) for sub in unique_subarrays]
    return result