def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def generate_sublists(circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublists.append(circular_list[i:j])
        return sublists
    sublists = generate_sublists(circular_list)
    result = [sublist for sublist in sublists if get_product(sublist) == 42]
    return result