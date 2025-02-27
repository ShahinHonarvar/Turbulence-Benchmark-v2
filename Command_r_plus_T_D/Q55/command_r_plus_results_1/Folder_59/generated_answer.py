def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -3

    def get_contiguous_sublists(circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublists.append(circular_list[j % len(circular_list):(j + 1) % len(circular_list) + 1])
        return sublists
    contiguous_sublists = get_contiguous_sublists(circular_list)
    result = [sublist for sublist in contiguous_sublists if product_equal_n(sublist)]
    return result