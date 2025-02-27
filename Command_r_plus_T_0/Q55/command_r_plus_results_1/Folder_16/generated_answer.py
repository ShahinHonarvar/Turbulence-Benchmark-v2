def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start] * arr[end] == product:
                    result.append(arr[start:end + 1])
        return result
    subarrays = find_subarrays(circular_list, -837)
    circular_subarrays = []
    for subarray in subarrays:
        for i in range(len(subarray)):
            circular_subarrays.append(subarray[i:] + subarray[:i])
    return circular_subarrays