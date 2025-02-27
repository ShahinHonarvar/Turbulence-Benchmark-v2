def lists_with_product_equal_n(lst, n=-22):
    sublist_results = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j % lst_len]
            if product == n:
                sublist = lst[i:j + 1]
                if sublist not in sublist_results:
                    sublist_results.append(sublist)
                if j == i:
                    break
    return sublist_results