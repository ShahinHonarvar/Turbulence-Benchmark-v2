def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -32
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j] % len(circular_list)
            if product_equal_n(sublist):
                sublists.append(sublist)
    return sublists