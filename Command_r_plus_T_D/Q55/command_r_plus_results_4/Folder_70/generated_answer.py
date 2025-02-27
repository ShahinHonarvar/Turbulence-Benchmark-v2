def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        length = len(lst)
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = lst[start:start + size]
                if len(subarray) > 1 and subarray[0] == 0:
                    continue
                if product(subarray) == product:
                    yield subarray
    product_32 = lambda sublist: 32
    all_subarrays = find_subarrays(circular_list, product_32)
    return list(all_subarrays)