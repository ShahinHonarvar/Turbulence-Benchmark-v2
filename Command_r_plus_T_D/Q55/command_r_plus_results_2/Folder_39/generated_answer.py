def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(circular_list):
        n = len(circular_list)
        for size in range(1, n + 1):
            for start in range(0, n):
                yield circular_list[start:start + size]
    product_sublists = []
    for sublist in get_contiguous_sublists(circular_list):
        if len(sublist) > 1 and sublist[0] != 0 and (sublist[-1] != 0):
            product = 1
            for num in sublist:
                product *= num
            if product == -46:
                product_sublists.append(sublist)
    return product_sublists