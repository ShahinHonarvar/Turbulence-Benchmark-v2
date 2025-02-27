def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(product_target: int, list_length: int) -> list[list[int]]:
        sublists = []
        for i in range(list_length):
            for j in range(i + 1, list_length + 1):
                sublist = circular_list[i:j]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    product_target = -69
    list_length = len(circular_list)
    all_sublists = find_sublists_with_product(product_target, list_length)
    return all_sublists