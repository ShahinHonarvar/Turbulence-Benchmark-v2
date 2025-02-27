def lists_with_product_equal_n(lst):
    sublists = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == -779:
                sublists.append(lst[i:j + 1 % length])
    return sublists