def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = arr[start:start + size]
                if product(subarray) == product:
                    result.append(subarray)
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, 85))
    return result