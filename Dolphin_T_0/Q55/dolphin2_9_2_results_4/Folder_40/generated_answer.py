def lists_with_product_equal_n(lst, n=-9):
    sublists = []
    for i in range(len(lst)):
        for end in range(i + 1, len(lst) + 1):
            product = 1
            for number in lst[i:end]:
                product *= number
            if i + end - 1 == len(lst) and product == n:
                sublist = lst[i:end] + lst[0:i]
                sublists.append(sublist)
    return sublists