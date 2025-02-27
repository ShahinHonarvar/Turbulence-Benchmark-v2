def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result

    def contiguous_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublists.append(lst[i:j + 1])
        return sublists
    sublists = contiguous_sublists(lst + lst)
    result = []
    for i in sublists:
        if product(i) == 632:
            if i in lst:
                result.append(i)
    return result