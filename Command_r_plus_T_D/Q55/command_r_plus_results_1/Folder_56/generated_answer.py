def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        length = len(lst)
        return [lst[i:j] for i in range(length) for j in range(i + 1, length + 1)]

    def product_equal_n(lst: list[int]) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == -65
    all_sublists = get_contiguous_sublists(circular_list)
    sublists_with_product_n = [sublist for sublist in all_sublists if product_equal_n(sublist)]
    return sublists_with_product_n