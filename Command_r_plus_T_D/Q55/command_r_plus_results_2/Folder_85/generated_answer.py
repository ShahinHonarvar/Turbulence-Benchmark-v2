def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            product = 1
            subarray = []
            for j in range(i, min(i + n, len(arr))):
                product *= arr[j]
                subarray.append(arr[j])
                if product == target:
                    result.append(subarray)
        return result
    n = len(circular_list)
    target_product = -97
    max_subarray_length = n
    all_subarrays = []
    for i in range(n):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], target_product, max_subarray_length)
        all_subarrays.extend(subarrays)
    return all_subarrays