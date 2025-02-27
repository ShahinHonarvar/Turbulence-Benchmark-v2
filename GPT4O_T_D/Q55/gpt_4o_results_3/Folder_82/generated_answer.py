def lists_with_product_equal_n(circular_list):

    def get_product_sublist(lst, start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= lst[i % len(lst)]
            sublist.append(lst[i % len(lst)])
            if product > 8:
                break
        return sublist if product == 8 else None
    results = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = get_product_sublist(circular_list, i, j)
            if sublist is not None:
                results.append(sublist)
    return results