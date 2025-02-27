def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    product_list = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j] % list_length
            if get_sublist_product(sublist) == -18:
                product_list.append(sublist)
    return product_list