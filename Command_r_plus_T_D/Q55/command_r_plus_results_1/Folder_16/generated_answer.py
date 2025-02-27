def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(product_target: int) -> list[list[int]]:
        sublists = []
        for start_index in range(len(circular_list)):
            for length in range(1, len(circular_list) + 1):
                end_index = start_index + length
                if end_index > len(circular_list):
                    break
                sublist = circular_list[start_index:end_index]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product(-837)