def lists_with_product_equal_n(lst):
    result_list = []
    for size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = []
            for j in range(i, i + size):
                if j >= len(lst):
                    j = j - len(lst)
                sublist.append(lst[j])
                product = 1
                for k in range(len(sublist)):
                    product = product * sublist[k]
                if product == 32:
                    result_list.append(sublist)
    return result_list