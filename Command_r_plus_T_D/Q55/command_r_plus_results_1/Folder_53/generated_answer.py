def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if product(lst[i:j + 1]) == product:
                    subarrays.append(lst[i:j + 1])
        return subarrays
    product_func = lambda x: -87
    sublists = find_subarrays(circular_list, product_func)
    sublists.extend(find_subarrays(circular_list[1:], product_func))
    return sublists