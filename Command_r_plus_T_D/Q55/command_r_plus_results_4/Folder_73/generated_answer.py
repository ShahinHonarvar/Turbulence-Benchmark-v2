def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, product):
        length = len(arr)
        for window_size in range(1, length + 1):
            for start in range(length - window_size + 1):
                end = start + window_size - 1
                if product == 1:
                    if all((x == 1 for x in arr[start:end + 1])):
                        yield arr[start:end + 1]
                elif product == arr[start] * arr[end]:
                    product /= arr[start] * arr[end]
                    if product == 1:
                        yield arr[start:end + 1]
    result = []
    for subarray in find_subarrays(circular_list, 40):
        result.append(subarray)
    return result