def lists_with_product_equal_n(circular_list):

    def get_sublist_products(start_index, product=1):
        sublist = []
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 33:
                yield sublist
                product = 1
                sublist = []
        if sublist:
            yield sublist
    result = []
    for i in range(len(circular_list)):
        result.extend(get_sublist_products(i))
    return result