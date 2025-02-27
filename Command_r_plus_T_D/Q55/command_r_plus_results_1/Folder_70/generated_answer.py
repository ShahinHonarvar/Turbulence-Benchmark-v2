def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start, product_so_far):
        if product_so_far == 32:
            return [subarray]
        subarrays = []
        for i in range(start, len(circular_list)):
            product_so_far *= circular_list[i]
            subarray.append(circular_list[i])
            subarrays_from_i = find_subarrays(i + 1, product_so_far)
            if subarrays_from_i:
                subarrays.extend(subarrays_from_i)
            product_so_far //= circular_list[i]
            subarray.pop()
        return subarrays
    all_subarrays = []
    for i in range(len(circular_list)):
        subarray = [circular_list[i]]
        all_subarrays.extend(find_subarrays(i + 1, circular_list[i]))
    return all_subarrays