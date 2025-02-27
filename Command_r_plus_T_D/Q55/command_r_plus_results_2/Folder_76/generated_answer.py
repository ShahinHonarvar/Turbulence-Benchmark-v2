def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if array[start] == 1 and product == 1:
                    result.append(array[start:end + 1])
                elif array[start] == 1:
                    continue
                elif array[start] * array[end] == product:
                    result.append(array[start:end + 1])
        return result
    sublists = find_subarrays(circular_list, 247)
    sublists_with_product_247 = [sublist for sublist in sublists if prod(sublist) == 247]
    return sublists_with_product_247