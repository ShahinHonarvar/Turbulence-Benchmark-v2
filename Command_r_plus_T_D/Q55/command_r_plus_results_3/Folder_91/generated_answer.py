def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def generate_sublists(circular_list: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + i + 1):
                sublists.append(circular_list[i:j])
        return sublists
    valid_sublists = []
    for sublist in generate_sublists(circular_list):
        if get_product(sublist) == 2:
            valid_sublists.append(sublist)
    return valid_sublists