def lists_with_product_equal_n(lst):
    sublists = []

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if product(sublist) == -779:
                sublists.append(sublist)
    return sublists