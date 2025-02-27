def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_subarray(start, product):
        current_product = circular_list[start]
        subarray = [circular_list[start]]
        i = start + 1
        while i != start:
            current_product *= circular_list[i]
            subarray.append(circular_list[i])
            if current_product == product:
                return subarray
            i = (i + 1) % len(circular_list)
        return []
    result = []
    for i in range(len(circular_list)):
        subarray = find_product_subarray(i, -76)
        if subarray:
            result.append(subarray)
    return result