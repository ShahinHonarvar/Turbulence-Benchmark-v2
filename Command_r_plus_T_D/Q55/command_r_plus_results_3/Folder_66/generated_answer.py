def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_to_seventy_eight(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 78
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equal_to_seventy_eight(sublist):
                sublists.append(sublist)
    return sublists