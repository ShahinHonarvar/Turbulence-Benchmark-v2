def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(product, subarray, circular_list):
        if product == -33:
            result.append(subarray)
        for i in range(len(circular_list)):
            new_product = product * circular_list[i]
            new_subarray = subarray + [circular_list[i]]
            find_subarrays(new_product, new_subarray, circular_list[i + 1:] + circular_list[:i + 1])
    result = []
    find_subarrays(1, [], circular_list)
    return result