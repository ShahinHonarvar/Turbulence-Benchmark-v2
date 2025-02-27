def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists(circular_list: list[int], product_n: int) -> list[list[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, len(circular_list) + i):
                sublist = circular_list[i:j]
                if len(sublist) <= len(circular_list) and get_product(sublist) == product_n:
                    sublists.append(sublist)
        return sublists
    product_48_sublists = find_sublists(circular_list, 48)
    return product_48_sublists