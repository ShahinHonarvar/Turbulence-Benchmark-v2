def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == 28:
            result.append(product_sublists)
        if start_index < len(circular_list) - 1 and product_so_far <= 28:
            find_product_sublists(start_index + 1, product_so_far)
        if start_index == len(circular_list) - 1 and product_so_far < 28:
            find_product_sublists(0, product_so_far)
    result = []
    for i in range(len(circular_list)):
        find_product_sublists(i, 1)
    return result