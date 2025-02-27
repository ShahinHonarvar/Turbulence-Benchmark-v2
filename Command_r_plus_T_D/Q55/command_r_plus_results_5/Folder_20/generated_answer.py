def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def product_of_sublist(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    all_sublists = get_contiguous_sublists(circular_list)
    result = [sublist for sublist in all_sublists if product_of_sublist(sublist) == -69]
    return result