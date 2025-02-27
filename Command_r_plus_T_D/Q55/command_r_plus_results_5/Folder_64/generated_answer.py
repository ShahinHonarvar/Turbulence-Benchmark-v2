def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def check_product(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 3

    def generate_sublists(clist: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(clist)):
            for j in range(i + 1, len(clist) + i + 1):
                sublists.append(clist[i:j % len(clist)])
        return sublists
    all_sublists = generate_sublists(circular_list)
    valid_sublists = [sublist for sublist in all_sublists if check_product(sublist)]
    return valid_sublists