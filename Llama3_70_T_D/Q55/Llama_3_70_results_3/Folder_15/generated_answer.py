def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            sublist = []
            for j in range(i, len(lst)):
                sublist.append(lst[j])
                sublists.append(sublist[:])
            sublist = []
            for j in range(i):
                sublist.append(lst[j])
                sublists.append(sublist[:])
        return sublists

    def get_sublists_with_product_n(sublists, n):
        sublists_with_product_n = []
        for sublist in sublists:
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists_with_product_n.append(sublist)
        return sublists_with_product_n
    sublists = get_sublists(lst)
    return get_sublists_with_product_n(sublists, -7)