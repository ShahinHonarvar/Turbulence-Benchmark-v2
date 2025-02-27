def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_five = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) > len(circular_list):
                break
            if sublist and sublist[-1] * sublist[0] == 5:
                products_equal_to_five.append(sublist)
    return products_equal_to_five