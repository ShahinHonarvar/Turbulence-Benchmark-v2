def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if lst[i:j + 1] not in subarrays and product(lst[i:j + 1]) == product:
                    subarrays.append(lst[i:j + 1])
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    sublists = find_subarrays(circular_list, -8)
    return sublists