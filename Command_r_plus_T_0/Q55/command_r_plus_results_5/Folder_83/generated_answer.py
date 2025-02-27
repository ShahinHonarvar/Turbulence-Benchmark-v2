def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start] == 0 and product != 0:
                    continue
                if arr[start] < 0 and (product % 2 == 0 or (product % 2 == 0 and product != 0)):
                    continue
                if arr[start] * arr[end] == product and all((num == 0 for num in arr[start + 1:end])):
                    result.append(arr[start:end + 1])
        return result
    subarrays = find_subarrays(circular_list, -57)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        circular_subarrays.append(subarray + [circular_list[0]])
        circular_subarrays.append([circular_list[-1]] + subarray)
        circular_subarrays.append([circular_list[-1], circular_list[0]] + subarray)
    unique_subarrays = []
    for subarray in circular_subarrays:
        subarray_tuple = tuple(subarray)
        if subarray_tuple not in unique_subarrays:
            unique_subarrays.append(subarray_tuple)
    return [list(subarray) for subarray in unique_subarrays]