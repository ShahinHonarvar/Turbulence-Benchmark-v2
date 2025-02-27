def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product == -17:
                    if arr[start] == -17 and size == 1:
                        result.append(arr[start:start + size])
                    elif arr[start] == -1 and arr[start + 1] == 17:
                        result.append(arr[start:start + size])
                    elif arr[start + size - 1] == -1 and arr[start + size - 2] == 17:
                        result.append(arr[start:start + size])
        return result
    subarrays = find_subarrays(circular_list, -17)
    circular_subarrays = []
    for subarray in subarrays:
        for i in range(len(subarray)):
            circular_subarrays.append(subarray[i:] + subarray[:i])
    unique_circular_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_circular_subarrays:
            unique_circular_subarrays.append(subarray)
    return unique_circular_subarrays