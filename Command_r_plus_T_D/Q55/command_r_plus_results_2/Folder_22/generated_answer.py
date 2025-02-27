def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if product(lst[i:j + 1]) == product:
                    subarrays.append(lst[i:j + 1])
        return subarrays
    product_4 = lambda x: 4
    all_subarrays = find_subarrays(circular_list, product_4)
    unique_subarrays = []
    for subarray in all_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays