def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists(start_index: int, product_so_far: int) -> list[list[int]]:
        sublists = []
        for i in range(start_index, len(circular_list) + start_index):
            product_so_far *= circular_list[i % len(circular_list)]
            if product_so_far == 48:
                sublists.append(circular_list[start_index:i % len(circular_list) + 1])
            elif product_so_far > 48 or i % len(circular_list) == start_index:
                break
        return sublists
    sublists = []
    for i in range(len(circular_list)):
        sublists_from_index = find_sublists(i, 1)
        sublists.extend(sublists_from_index)
    return sublists