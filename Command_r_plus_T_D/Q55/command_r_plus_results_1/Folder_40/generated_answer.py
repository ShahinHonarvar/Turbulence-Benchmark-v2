def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start_index, product_so_far):
        if product_so_far == -9:
            return [subarray]
        subarrays = []
        for i in range(start_index, len(circular_list)):
            product_so_far *= circular_list[i]
            if product_so_far == -9:
                subarrays.append(circular_list[start_index:i + 1])
            elif product_so_far % -9 == 0:
                subarrays.extend(find_subarrays(i + 1, product_so_far // -9))
        return subarrays
    all_subarrays = []
    for i in range(len(circular_list)):
        all_subarrays.extend(find_subarrays(i, circular_list[i]))
    return all_subarrays