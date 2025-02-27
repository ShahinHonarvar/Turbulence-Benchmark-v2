def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if prod(array[start:start + size]) == product:
                    result.append(array[start:start + size])
        return result

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    subarrays = find_subarrays(circular_list, 3)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        for i in range(1, len(subarray)):
            circular_subarrays.append(subarray[i:] + subarray[:i])
    return circular_subarrays