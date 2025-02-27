def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product == -1:
                    if arr[start] < 0:
                        result.append(arr[start:start + size])
                    elif any((x < 0 for x in arr[start + 1:start + size])):
                        result.append(arr[start:start + size])
        return result
    subarrays = find_subarrays(circular_list, -17)
    subarrays_with_product_n = [sub for sub in subarrays if product(sub) == -17]
    return subarrays_with_product_n