def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product(arr[start:start + size]) == -3:
                    result.append(arr[start:start + size])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    subarrays = find_subarrays(circular_list, product)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarray = subarray.copy()
        circular_subarray.append(circular_subarray[0])
        circular_subarrays.append(circular_subarray)
    return circular_subarrays