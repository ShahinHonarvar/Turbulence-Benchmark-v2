def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equals_seventy_four(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 74
    all_sublists = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equals_seventy_four(sublist):
                all_sublists.append(sublist)
    return all_sublists