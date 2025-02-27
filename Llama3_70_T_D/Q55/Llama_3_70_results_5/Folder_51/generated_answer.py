def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

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
    sublists = get_sublists(lst)
    return [sublist for sublist in sublists if product(sublist) == -44]