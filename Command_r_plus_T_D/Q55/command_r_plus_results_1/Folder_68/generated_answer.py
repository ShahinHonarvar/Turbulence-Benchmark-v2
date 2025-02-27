def lists_with_product_equal_n(circular_list):

    def product_equal_6(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 6
    all_sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j] % len(circular_list)
            all_sublists.append(sublist)
    valid_sublists = [sublist for sublist in all_sublists if product_equal_6(sublist)]
    return valid_sublists