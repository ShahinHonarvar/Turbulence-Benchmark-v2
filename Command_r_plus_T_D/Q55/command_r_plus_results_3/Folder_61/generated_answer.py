def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists(lst: list[int], product_target: int) -> list[list[int]]:
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublist = lst[i:j + 1]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    all_products = []
    for i in range(len(circular_list)):
        rotated_list = circular_list[i:] + circular_list[:i]
        all_products.extend(find_sublists(rotated_list, -10))
    return all_products