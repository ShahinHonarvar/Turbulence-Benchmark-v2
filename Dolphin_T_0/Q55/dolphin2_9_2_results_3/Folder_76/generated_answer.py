def lists_with_product_equal_n(lst):

    def product_of_sublist(sublist):
        p = 1
        for x in sublist:
            p *= x
        return p
    n = 247
    length = len(lst)
    result = []
    for length_sublist in range(1, length + 1):
        for i in range(length):
            if length_sublist > length:
                break
            sublist = lst[i:i + length_sublist]
            if product_of_sublist(sublist) == n:
                result.append(sublist)
    return result