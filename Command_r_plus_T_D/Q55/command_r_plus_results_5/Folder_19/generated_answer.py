def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_subarrays(arr, target_product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = arr[start:start + size]
                if len(subarray) > 1 and subarray[0] == 0 and (subarray[-1] == 0):
                    continue
                if product(subarray) == target_product:
                    result.append(subarray)
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_product_subarrays(temp_list, -54))
    return result