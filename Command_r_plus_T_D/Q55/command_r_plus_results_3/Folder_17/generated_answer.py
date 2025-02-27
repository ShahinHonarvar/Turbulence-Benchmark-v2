def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_18 = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and sublist not in products_equal_to_18:
                product = 1
                for num in sublist:
                    product *= num
                if product == 18:
                    products_equal_to_18.append(sublist)
    return products_equal_to_18