def lists_with_product_equal_n(lst):
    results = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j % lst_len]
            if product == 78:
                temp = []
                for k in range(i, j + 1):
                    temp.append(lst[k % lst_len])
                results.append(temp)
    return results