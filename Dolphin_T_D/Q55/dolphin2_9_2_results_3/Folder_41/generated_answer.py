def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    products_equal_n = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            product = 1
            if sublist == sublist[::-1]:
                for num in sublist:
                    product *= num
            else:
                for num in sublist:
                    for num2 in sublist[sublist.index(num) + 1:]:
                        product *= num * num2
            if product == -20:
                products_equal_n.append(sublist)
    return products_equal_n