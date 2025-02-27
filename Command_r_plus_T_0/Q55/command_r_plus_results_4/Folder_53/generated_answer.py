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
        rotated_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(rotated_list, -87, len(circular_list)))
    return result