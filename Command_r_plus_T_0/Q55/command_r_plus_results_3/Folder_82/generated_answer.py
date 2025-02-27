def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1 and size > 1:
                    break
                if product == 1 or arr[start] == product:
                    result.append(arr[start:start + size])
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, 8))
    return result