def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_sublist_product(start_index, product_so_far):
        product_so_far *= circular_list[start_index]
        if product_so_far == -779:
            result.append(list(sublist_product))
        for i in range(start_index + 1, len(circular_list) + start_index + 1):
            sublist_product.append(circular_list[i % len(circular_list)])
            find_sublist_product(i % len(circular_list), product_so_far)
            sublist_product.pop()
    result = []
    for i in range(len(circular_list)):
        sublist_product = [circular_list[i]]
        find_sublist_product(i, 1)
    return result