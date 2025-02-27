def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -93
    all_sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j] % len(circular_list)
            if product_equal_n(sublist):
                all_sublists.append(sublist)
    return all_sublists