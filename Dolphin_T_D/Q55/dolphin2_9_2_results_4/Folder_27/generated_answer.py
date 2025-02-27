def lists_with_product_equal_n(lst):
    result = []
    size_lst = len(lst)
    for size_sublist in range(1, size_lst + 1):
        for i in range(size_lst):
            product = 1
            sublist = []
            for j in range(size_sublist):
                sublist.append(lst[(i + j) % size_lst])
                product *= sublist[-1]
            if product == -82:
                result.append(sublist)
    return result