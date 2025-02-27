def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_99 = lambda x: 99
    sublists = find_subarrays(circular_list, product_99)
    sublists.extend(find_subarrays(circular_list[1:], product_99))
    return sublists