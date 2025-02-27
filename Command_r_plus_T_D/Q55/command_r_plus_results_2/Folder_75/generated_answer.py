def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product_13(circular_list: list[int]) -> list[list[int]]:
        size = len(circular_list)
        all_sublists = []
        for length in range(1, size + 1):
            for start in range(0, size):
                end = start + length
                if end <= size:
                    sublist = circular_list[start:end]
                    if get_sublist_product(sublist) == 13:
                        all_sublists.append(sublist)
                else:
                    sublist = circular_list[start:] + circular_list[:end % size]
                    if get_sublist_product(sublist) == 13:
                        all_sublists.append(sublist)
        return all_sublists
    return find_sublists_with_product_13(circular_list)