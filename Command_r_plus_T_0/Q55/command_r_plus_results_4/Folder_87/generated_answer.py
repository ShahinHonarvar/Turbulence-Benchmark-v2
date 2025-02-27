def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start_index: int, product_so_far: int) -> list[list[int]]:
        subarrays = []
        product = product_so_far * circular_list[start_index]
        if product == 27:
            subarrays.append(circular_list[start_index - 1:start_index + 1])
        if start_index == len(circular_list) - 1:
            return subarrays
        for i in range(start_index + 1, len(circular_list) + 1):
            subarrays_from_i = find_subarrays(i % len(circular_list), product)
            if subarrays_from_i:
                subarrays.extend(subarrays_from_i)
        return subarrays
    all_subarrays = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(i, 1)
        all_subarrays.extend(subarrays)
    return all_subarrays