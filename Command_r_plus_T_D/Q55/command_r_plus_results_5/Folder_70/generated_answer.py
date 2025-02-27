def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product % arr[start] == 0:
                    if product // arr[start] == 1:
                        result.append(arr[start:start + size])
                    else:
                        find_subarrays(arr[start + 1:start + size], product // arr[start])
        return result
    product = 32
    result = []
    for i in range(len(circular_list)):
        temp = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp, product))
    return result