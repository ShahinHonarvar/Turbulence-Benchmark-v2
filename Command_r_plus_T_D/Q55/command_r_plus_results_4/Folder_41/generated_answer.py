def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -20

    def generate_sublists(circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublists.append(circular_list[i:j])
        return sublists
    return [sublist for sublist in generate_sublists(circular_list) if product_equal_n(sublist)]