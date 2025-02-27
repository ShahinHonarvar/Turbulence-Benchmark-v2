def lists_with_product_equal_n(lst):
    n = 25
    len_lst = len(lst)
    lst += lst[:len_lst // 2]
    result = []
    for start in range(len_lst):
        product = 1
        for end in range(start, start + len_lst):
            product *= lst[end % len_lst]
            if product == n:
                result.append(lst[start:end % len_lst + 1])
            elif product > n:
                break
    return result