def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 93
    n = len(circular_list)
    all_sublists = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j]
            if product_equal_n(sublist):
                all_sublists.append(sublist)
    return all_sublists