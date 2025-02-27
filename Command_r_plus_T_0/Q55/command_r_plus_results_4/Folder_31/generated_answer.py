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
                    elif arr[start + size - 1] < 0:
                        result.append(arr[start:start + size])
                elif arr[start] * arr[start + size - 1] < 0:
                    if product % arr[start] == 0 and product // arr[start] in arr[start + 1:start + size]:
                        result.append(arr[start:start + size])
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, -16))
    return result