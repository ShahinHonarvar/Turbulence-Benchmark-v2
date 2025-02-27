def lists_with_product_equal_n(lst):
    product_of_sublist = 851
    size_of_sublist = len(lst)
    results = []
    n_lst = lst * 2
    for size in range(1, size_of_sublist + 1):
        for idx in range(len(n_lst)):
            if n_lst[idx] * n_lst[idx + 1] * ... * n_lst[idx + size - 1] == product_of_sublist:
                results.append(n_lst[idx:idx + size])
    return results