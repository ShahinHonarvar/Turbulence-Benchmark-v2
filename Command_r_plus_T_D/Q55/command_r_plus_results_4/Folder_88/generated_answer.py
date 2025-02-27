def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    target_product = -56
    list_length = len(circular_list)
    all_sublists = []
    for i in range(list_length):
        for j in range(i, i + list_length):
            sublist = circular_list[i:j]
            if get_product(sublist) == target_product:
                all_sublists.append(sublist)
    return all_sublists