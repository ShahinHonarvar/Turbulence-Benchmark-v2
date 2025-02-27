def lists_with_product_equal_n(circular_list):
    sublists = []
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list) + 1):
            sublist = circular_list[start:end]
            product = 1
            for num in sublist:
                product *= num
            if product == 32:
                sublists.append(sublist)
    return sublists