def lists_with_product_equal_n(lst, n):
    size = len(lst)
    result = []
    product_window = 1
    for i in range(size):
        for j in range(i, i + size):
            j_index = j % size
            product_window *= lst[j_index]
            product_window %= n
            if product_window % n == 0:
                result.append(lst[i:j_index + 1])
    return result