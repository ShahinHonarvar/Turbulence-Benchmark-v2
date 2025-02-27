def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start, product_so_far):
        if product_so_far == -8:
            result.append(subarray[:])
        for i in range(start, len(circular_list)):
            subarray.append(circular_list[i])
            find_subarrays(i + 1, product_so_far * circular_list[i])
            subarray.pop()
    result = []
    subarray = []
    find_subarrays(0, 1)
    return result