def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(target_product: int) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublist = circular_list[i:j]
                if get_sublist_product(sublist) == target_product:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product(-838)