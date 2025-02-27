def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -30
    n = len(circular_list)
    all_sublists = []
    for size in range(1, n + 1):
        for start in range(n):
            end = start + size
            sublist = circular_list[start:end]
            if product_equal_n(sublist):
                all_sublists.append(sublist)
    return all_sublists