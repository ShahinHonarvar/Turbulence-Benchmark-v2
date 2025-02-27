def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for i in range(length):
            for j in range(i, length):
                if j - i + 1 > length:
                    break
                if product(arr[i:j + 1]) == -65:
                    result.append(arr[i:j + 1])
        return result
    product_func = lambda x: -1 * reduce(lambda a, b: a * b, x, 1)
    subarrays = find_subarrays(circular_list, product_func)
    subarrays.extend(find_subarrays(circular_list[::-1], product_func))
    unique_subarrays = []
    for subarray in subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays