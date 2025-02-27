def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(len(lst)):
                product *= lst[(i + j) % len(lst)]
                sublist.append(lst[(i + j) % len(lst)])
                if product == -23:
                    sublists.append(sublist[:])
        return sublists
    result = get_sublists(lst)
    return result