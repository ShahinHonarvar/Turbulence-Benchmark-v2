def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if array[start] * array[end] == product:
                    result.append(array[start:end + 1])
        return result
    subarrays = find_subarrays(circular_list, -56)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        circular_subarrays.append(subarray + subarray[-1:])
        circular_subarrays.append(subarray[0] + subarray)
    unique_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays