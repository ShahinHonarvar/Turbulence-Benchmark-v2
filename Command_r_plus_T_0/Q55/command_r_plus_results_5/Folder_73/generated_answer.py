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
    result = []
    for i in range(len(circular_list)):
        for sublist in find_subarrays(circular_list, 40, len(circular_list)):
            result.append(sublist)
    return result