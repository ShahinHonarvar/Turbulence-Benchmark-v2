def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if product == 1:
                    if all((x == 1 for x in arr[start:end + 1])):
                        result.append(arr[start:end + 1])
                elif product == arr[start:end + 1].reduce(lambda x, y: x * y):
                    result.append(arr[start:end + 1])
        return result
    subarrays = find_subarrays(circular_list, -837)
    unique_subarrays = [list(x) for x in set((tuple(x) for x in subarrays))]
    return unique_subarrays