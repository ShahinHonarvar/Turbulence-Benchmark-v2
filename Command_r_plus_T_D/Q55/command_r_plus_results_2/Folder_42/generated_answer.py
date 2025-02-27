def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_25 = lambda x: 25
    product_125 = lambda x: 125
    sublists_25 = find_subarrays(circular_list, product_25)
    sublists_125 = find_subarrays(circular_list, product_125)
    result = []
    for sublist in sublists_25:
        if sublist in sublists_125:
            result.append(sublist)
    return result