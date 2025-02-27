def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        length = len(lst)
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    if lst[i] == product:
                        yield [lst[i]]
                else:
                    subarray = lst[i:j + 1]
                    if prod(subarray) == product:
                        yield subarray
    return list(find_subarrays(circular_list, -97))