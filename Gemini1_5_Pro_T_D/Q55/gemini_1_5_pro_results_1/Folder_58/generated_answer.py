def lists_with_product_equal_n(circular_list):
    n = 733
    sublists = []
    list_size = len(circular_list)
    for i in range(list_size):
        for j in range(i, list_size):
            sublist = circular_list[i:j + 1]
            if len(sublist) > list_size:
                break
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == n:
                sublists.append(sublist)
    for i in range(0, list_size - 1):
        for j in range(0, i):
            sublist = circular_list[i:list_size] + circular_list[0:j + 1]
            if len(sublist) > list_size:
                break
            product = 1
            for k in range(len(sublist)):
                product *= sublist[k]
            if product == n:
                sublists.append(sublist)
    return sublists