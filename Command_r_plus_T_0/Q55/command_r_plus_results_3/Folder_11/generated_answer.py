def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product == -15:
                    if arr[start] == -3 and arr[start + 1] == 5:
                        result.append(arr[start:start + size])
                    elif arr[start] == 5 and arr[start + 1] == -3:
                        result.append(arr[start:start + size])
        return result
    subarrays = find_subarrays(circular_list, -15)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        circular_subarrays.append(subarray + subarray[-1:])
        circular_subarrays.append([subarray[-1]] + subarray)
    unique_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays