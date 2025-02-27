def lists_with_product_equal_n(circular_list):

    def get_contiguous_sublists(lst):
        n = len(lst)
        for length in range(1, n + 1):
            for start in range(n):
                sublist = []
                for i in range(length):
                    sublist.append(lst[(start + i) % n])
                yield sublist
    sublists = []
    for sublist in get_contiguous_sublists(circular_list):
        product = 1
        for num in sublist:
            product *= num
        if product == -65:
            sublists.append(sublist)
    return sublists