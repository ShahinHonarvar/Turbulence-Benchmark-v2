def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start] == 0 and product != 0:
                    continue
                if arr[start] < 0 and (product % arr[start] == 0) ^ (product < 0):
                    continue
                if arr[start] * arr[end] == product and all((arr[start + i] == product // arr[start] for i in range(1, size - 1))):
                    result.append(arr[start:end + 1])
        return result
    result = []
    for i in range(len(circular_list)):
        rotated = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(rotated, -837))
    return result