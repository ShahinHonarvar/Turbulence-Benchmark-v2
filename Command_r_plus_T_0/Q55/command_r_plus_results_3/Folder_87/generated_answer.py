def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start_index: int, product_so_far: int) -> list[list[int]]:
        subarrays = []
        product = product_so_far
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            product *= circular_list[index]
            if product == 27:
                subarrays.append(circular_list[start_index:i + 1])
            if product > 27:
                break
        return subarrays
    subarrays = []
    for i in range(len(circular_list)):
        subarrays.extend(find_subarrays(i, 1))
    return subarrays