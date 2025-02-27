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
    subarrays = find_subarrays(circular_list, -69, len(circular_list))
    circular_subarrays = []
    for subarray in subarrays:
        for i in range(len(subarray)):
            circular_subarray = subarray[i:] + subarray[:i]
            circular_subarrays.append(circular_subarray)
    unique_circular_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_circular_subarrays:
            unique_circular_subarrays.append(subarray)
    return unique_circular_subarrays