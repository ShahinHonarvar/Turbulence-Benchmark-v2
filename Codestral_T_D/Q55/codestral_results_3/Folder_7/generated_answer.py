def lists_with_product_equal_n(lst):

    def circ_lst(i):
        return lst[i:] + lst[:i]

    def find_sublists(lst):
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == 537:
                    yield lst[i:j + 1]
    return [sublist for i in range(len(lst)) for sublist in find_sublists(circ_lst(i))]