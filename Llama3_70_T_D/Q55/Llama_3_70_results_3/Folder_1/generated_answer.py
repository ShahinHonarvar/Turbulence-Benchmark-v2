def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            sublist = []
            product = 1
            for j in range(i, n + i):
                sublist.append(lst[j % n])
                product *= lst[j % n]
                if product == -51:
                    sublists.append(sublist[:])
                elif product < -51:
                    break
        return sublists
    result = get_sublists(lst)
    return result