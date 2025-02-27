def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_equal_subarrays(array, product):
        subarrays = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                if product(array[i:j + 1]) == -1:
                    subarrays.append(array[i:j + 1])
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    subarrays = find_product_equal_subarrays(circular_list, product)
    return subarrays