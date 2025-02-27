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
    subarrays = find_subarrays(circular_list, -5)
    unique_subarrays = [tuple(sub) for sub in subarrays]
    unique_subarrays = list(set(unique_subarrays))
    unique_subarrays = [list(sub) for sub in unique_subarrays]
    return unique_subarrays