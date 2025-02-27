def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        length = len(lst)
        sublists = []
        for size in range(1, length + 1):
            for start in range(length):
                end = start + size
                sublists.append(lst[start:end])
        return sublists

    def product_equals_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -61
    all_sublists = get_contiguous_sublists(circular_list)
    result = [sublist for sublist in all_sublists if product_equals_n(sublist)]
    return result