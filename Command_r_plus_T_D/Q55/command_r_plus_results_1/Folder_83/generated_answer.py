def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + n, len(arr))):
                if prod(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    if not circular_list:
        return []
    circular_list_length = len(circular_list)
    max_subarray_length = circular_list_length // 2
    all_subarrays = []
    for i in range(circular_list_length):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], -57, max_subarray_length)
        all_subarrays.extend(subarrays)
    unique_subarrays = []
    for subarray in all_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays