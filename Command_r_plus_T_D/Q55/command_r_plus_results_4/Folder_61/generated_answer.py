def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists(circular_list: list[int], product_target: int) -> list[list[int]]:
        length = len(circular_list)
        sublists = []
        for size in range(1, length + 1):
            for start in range(0, length):
                end = start + size - 1 if start + size - 1 < length else start + size - 1 - length
                sublist = circular_list[start:end + 1]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    product_target = -10
    all_sublists = find_sublists(circular_list, product_target)
    return all_sublists