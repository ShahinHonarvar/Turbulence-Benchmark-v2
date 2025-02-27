def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        length = len(array)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if array[start] == 0 and product != 0:
                    continue
                if array[start] < 0 and (product % 2 == 0 or size % 2 == 0):
                    continue
                if array[start] > 0 and product < 0:
                    continue
                if array[start] * array[end] % product == 0:
                    temp = array[start:end + 1]
                    if temp not in result:
                        result.append(temp)
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, -91))
    return result