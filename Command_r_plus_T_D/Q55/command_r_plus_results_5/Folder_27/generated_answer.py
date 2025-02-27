def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(product_target: int, circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublist = circular_list[i:j]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    product_target = -82
    all_sublists = find_sublists_with_product(product_target, circular_list)
    unique_sublists = []
    for sublist in all_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists