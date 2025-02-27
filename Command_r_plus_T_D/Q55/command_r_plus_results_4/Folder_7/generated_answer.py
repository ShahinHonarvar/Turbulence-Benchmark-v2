def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if lst[i:j + 1] not in result and product(lst[i:j + 1]) == product:
                    result.append(lst[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return find_subarrays(circular_list, 537)