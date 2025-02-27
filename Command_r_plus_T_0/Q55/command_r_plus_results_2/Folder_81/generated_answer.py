def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                else:
                    prod = 1
                    for i in range(start, start + size):
                        prod *= arr[i]
                    if prod == product:
                        result.append(arr[start:start + size])
        return result
    subarrays = find_subarrays(circular_list, -8)
    unique_subarrays = []
    for subarray in subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays