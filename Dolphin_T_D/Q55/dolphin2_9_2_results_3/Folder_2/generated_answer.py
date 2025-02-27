def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    product_dict = {}
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= circular_list[j]
            if product in product_dict:
                result.append(circular_list[product_dict[product]:j + 1])
            else:
                product_dict[product] = j + 1
    for i in range(n):
        product = 1
        for j in range(i, -1, -1):
            product *= circular_list[j]
            if product in product_dict:
                result.append(circular_list[product_dict[product]:i])
            else:
                product_dict[product] = j
    return result