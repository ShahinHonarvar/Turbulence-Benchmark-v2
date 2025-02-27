def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for i in range(length):
            product_so_far = 1
            for j in range(i, length):
                product_so_far *= array[j % length]
                if product_so_far == product:
                    result.append(array[i:j + 1])
                if product_so_far * array[(j + 1) % length] == product:
                    result.append(array[i:j + 2])
        return result
    subarrays = find_subarrays(circular_list, -17)
    unique_subarrays = []
    for subarray in subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays