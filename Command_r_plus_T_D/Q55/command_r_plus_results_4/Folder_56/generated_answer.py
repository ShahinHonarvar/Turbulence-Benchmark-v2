def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        length = len(lst)
        sublists = []
        for size in range(1, length + 1):
            for start in range(length):
                end = start + size
                sublists.append(lst[start:end])
        return sublists

    def product_of_sublist(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    target_product = -65
    all_sublists = get_contiguous_sublists(circular_list)
    valid_sublists = [sublist for sublist in all_sublists if product_of_sublist(sublist) == target_product]
    return valid_sublists