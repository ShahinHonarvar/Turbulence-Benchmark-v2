def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = array[start:start + size]
                if len(subarray) > 1 and subarray[0] == 0 and (subarray[-1] == 0):
                    continue
                if product(subarray) == product:
                    result.append(subarray)
        return result
    result = find_subarrays(circular_list, -837)
    if len(result) == 0:
        result = find_subarrays(circular_list + circular_list, -837)
    return result