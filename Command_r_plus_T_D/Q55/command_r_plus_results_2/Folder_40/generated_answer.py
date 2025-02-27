def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product == arr[start] and all((x == 1 for x in arr[start + 1:start + size])):
                    result.append(arr[start:start + size])
                elif product == arr[start + size - 1] and all((x == 1 for x in arr[start:start + size - 1])):
                    result.append(arr[start:start + size])
                elif product == arr[start] * arr[start + size - 1] and all((x == 1 for x in arr[start + 1:start + size - 1])):
                    result.append(arr[start:start + size])
                elif product == arr[start] * arr[start + size - 1] and all((x == 1 for x in arr[start + 1:start + size - 1])):
                    result.append(arr[start:start + size])
        return result
    sublists = find_subarrays(circular_list, -9)
    unique_sublists = [list(x) for x in set((tuple(x) for x in sublists))]
    return unique_sublists