def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_equal_to_n(n: int, circular_list: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(circular_list)):
            product = 1
            sublist = []
            for j in range(i, len(circular_list) + i):
                product *= circular_list[j % len(circular_list)]
                sublist.append(circular_list[j % len(circular_list)])
                if product == n:
                    result.append(sublist)
        return result
    return find_product_equal_to_n(85, circular_list)