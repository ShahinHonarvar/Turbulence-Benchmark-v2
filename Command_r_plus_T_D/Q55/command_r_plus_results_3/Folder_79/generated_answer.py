def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        subarrays = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                if product(array[i:j + 1]) == product:
                    subarrays.append(array[i:j + 1])
        return subarrays

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    sublists = find_subarrays(circular_list, -83)
    sublists.extend(find_subarrays(circular_list[::-1], -83))
    return sublists