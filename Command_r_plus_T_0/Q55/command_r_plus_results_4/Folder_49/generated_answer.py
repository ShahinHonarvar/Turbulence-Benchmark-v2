def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, size):
        result = []
        for i in range(len(arr)):
            product = 1
            subarray = []
            for j in range(i, min(i + size, len(arr))):
                product *= arr[j]
                subarray.append(arr[j])
                if product == target_product:
                    result.append(subarray)
        return result
    result = []
    for size in range(1, len(circular_list) + 1):
        result.extend(find_subarrays(circular_list, -61, size))
    return result