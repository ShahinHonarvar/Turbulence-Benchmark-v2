def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start_index, product_so_far):
        if product_so_far == 93:
            result.append(subarray[:])
        for i in range(start_index, len(circular_list)):
            subarray.append(circular_list[i])
            find_subarrays(i + 1, product_so_far * circular_list[i])
            subarray.pop()
    result = []
    for i in range(len(circular_list)):
        find_subarrays(i, 1)
    return result