def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        for length_subarray in range(1, length + 1):
            for start_index in range(0, length - length_subarray + 1):
                end_index = start_index + length_subarray - 1
                subarray = array[start_index:end_index + 1]
                if len(subarray) == 1 and subarray[0] == 1:
                    continue
                if reduce(lambda x, y: x * y, subarray) == product:
                    yield subarray
    product_list = list(find_subarrays(circular_list, 100))
    return product_list