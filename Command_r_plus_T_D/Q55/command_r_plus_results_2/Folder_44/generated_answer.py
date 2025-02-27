def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        result = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    result.append(arr[i:j + 1])
        return result
    product_29 = lambda x: 29
    all_subarrays = find_subarrays(circular_list, product_29)
    unique_subarrays = [list(x) for x in set((tuple(x) for x in all_subarrays))]
    return unique_subarrays