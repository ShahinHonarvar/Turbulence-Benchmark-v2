def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_value = -968
    sublists = find_subarrays(circular_list, lambda x: product_value)
    sublists.extend(find_subarrays(circular_list[1:] + [circular_list[0]], lambda x: product_value))
    return sublists