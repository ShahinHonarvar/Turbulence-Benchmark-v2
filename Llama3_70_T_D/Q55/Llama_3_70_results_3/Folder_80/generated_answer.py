def lists_with_product_equal_n(lst):

    def get_all_sublists(lst):
        sublists = []
        length = len(lst)
        for i in range(length):
            for j in range(i + 1, i + length + 1):
                sublists.append(lst[i:j])
        return sublists

    def get_circular_sublists(lst):
        length = len(lst)
        sublists = []
        for i in range(length):
            for j in range(1, length + 1):
                sublists.append(lst[i:i + j])
                sublists.append(lst[i:] + lst[:j - (length - i)])
        return sublists

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product

    def filter_sublists(sublists):
        return [sublist for sublist in sublists if get_product(sublist) == 43]
    return filter_sublists(get_circular_sublists(lst))