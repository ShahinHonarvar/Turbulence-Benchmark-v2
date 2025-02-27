def product(sublist):
    product_value = 1
    for i in sublist:
        product_value *= i
    return product_value

def lists_with_product_equal_n(cirlist):
    sublists = []
    for i in range(len(cirlist)):
        for j in range(i + 1, len(cirlist)):
            sublist = cirlist[i:j + 1]
            if product(sublist) == -46:
                sublists.append(sublist)
    return sublists