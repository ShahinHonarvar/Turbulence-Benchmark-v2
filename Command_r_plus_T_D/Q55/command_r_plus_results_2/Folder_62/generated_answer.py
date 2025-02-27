def lists_with_product_equal_n(circular_list):

    def get_sublist_products(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i + 1, list_length + i + 1):
            sublist = circular_list[i:j] % list_length
            if get_sublist_products(sublist) == 100:
                result.append(sublist)
    return result