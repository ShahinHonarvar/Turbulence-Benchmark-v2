def lists_with_product_equal_n(circular_list):

    def find_product_sublists(lst, target_product):
        length = len(lst)
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length + i):
                product *= lst[j % length]
                sublist.append(lst[j % length])
                if product == target_product:
                    yield sublist
                    product = 1
                    sublist = []
    return list(find_product_sublists(circular_list, 714))