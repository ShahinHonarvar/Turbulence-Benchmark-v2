def lists_with_product_equal_n(lst):

    def get_all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
                sublists.append(lst[j:] + lst[:i])
        return sublists

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    sublists = get_all_sublists(lst)
    return [sublist for sublist in sublists if get_product(sublist) == -65]