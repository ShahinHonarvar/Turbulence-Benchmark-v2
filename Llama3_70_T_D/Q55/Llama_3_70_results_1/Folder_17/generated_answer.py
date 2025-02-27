def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(len(lst)):
            index = (i + j) % len(lst)
            product *= lst[index]
            sublist.append(lst[index])
            if product == 18 and sublist not in result:
                result.append(sublist[:])
            if product > 18:
                break
    return result