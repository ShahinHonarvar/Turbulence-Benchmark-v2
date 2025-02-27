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
    target = 537
    all_subarrays = []
    for i in range(n):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], target, n)
        all_subarrays.extend(subarrays)
    return all_subarrays