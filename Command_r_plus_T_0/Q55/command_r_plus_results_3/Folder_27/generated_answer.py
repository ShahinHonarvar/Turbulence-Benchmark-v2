def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + n, len(arr))):
                if prod(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def prod(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    subarrays = find_subarrays(circular_list, -82, len(circular_list))
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        circular_subarrays.append(subarray + [circular_list[0]])
        circular_subarrays.append([circular_list[-1]] + subarray)
    unique_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays