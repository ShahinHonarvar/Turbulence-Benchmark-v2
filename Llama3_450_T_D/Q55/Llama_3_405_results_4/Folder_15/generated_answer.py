def lists_with_product_equal_n(lst):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def get_all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        for i in range(len(lst)):
            for j in range(0, i):
                sublists.append(lst[i:] + lst[:j + 1])
        return sublists
    result = [sublist for sublist in get_all_sublists(lst) if get_product(sublist) == -7]
    return result