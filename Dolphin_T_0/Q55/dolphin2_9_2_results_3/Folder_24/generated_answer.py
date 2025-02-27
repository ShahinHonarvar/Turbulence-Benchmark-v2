def lists_with_product_equal_n(lst):

    def is_circular_sublist(lst, sublist):
        sublist = sublist + sublist[:1]
        return lst == sublist or lst[1:] == sublist

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    result = []
    size = len(lst)
    for length in range(1, size + 1):
        for i in range(size):
            subset = lst[i:i + length]
            if is_circular_sublist(lst, subset) and abs(product(subset)) == 89:
                result.append(subset)
    return result