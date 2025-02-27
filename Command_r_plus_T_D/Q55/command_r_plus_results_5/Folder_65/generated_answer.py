def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(product_target: int, circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + 1):
                sublist = circular_list[i:j]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product(46, circular_list)