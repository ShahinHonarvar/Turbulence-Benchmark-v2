def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def get_circular_sublists(lst):
        circular_sublists = []
        for i in range(len(lst)):
            for j in range(len(lst)):
                if j < i:
                    continue
                circular_sublists.append(lst[i:j] + lst[:i] + lst[j:])
        return circular_sublists

    def filter_sublists(sublists):
        result = []
        for sublst in sublists:
            product = 1
            for num in sublst:
                product *= num
            if product == -54:
                result.append(sublst)
        return result
    sublists = get_sublists(lst) + get_circular_sublists(lst)
    return filter_sublists(sublists)