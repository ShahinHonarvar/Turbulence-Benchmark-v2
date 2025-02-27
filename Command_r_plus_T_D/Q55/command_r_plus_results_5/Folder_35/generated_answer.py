def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if product(lst[i:j + 1]) == product:
                    subarrays.append(lst[i:j + 1])
        return subarrays
    product = lambda x: 83
    subarrays = find_subarrays(circular_list, product)
    subarrays.extend(find_subarrays(circular_list[::-1], product))
    return subarrays