def lists_with_product_equal_n(lst, n=-23):

    def is_product_n(sublist, n):
        product = 1
        for number in sublist:
            product *= number
        return product == n
    sublists = []
    for i in range(len(lst)):
        for subsequence in range(i + 1, len(lst) + 1):
            if is_product_n(lst[i:subsequence], n):
                sublists.append(lst[i:subsequence])
    return sublists