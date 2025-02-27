def lists_with_product_equal_n(input_list, n=-65):
    sublists = []
    for start in range(len(input_list)):
        for end in range(start + 1, len(input_list) + 1):
            product = 1
            for number in input_list[start:end]:
                product *= number
            if product == n:
                sublists.append(list(input_list[start:end]))
    return sublists