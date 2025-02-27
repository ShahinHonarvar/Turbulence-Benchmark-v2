def lists_with_product_equal_n(lst, n=10):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sub_lst = lst[i:j + 1]
            if i > 0:
                sub_lst = sub_lst + lst[:i]
            elif j < len(lst) - 1:
                sub_lst = sub_lst + lst[j + 1:]
            product = 1
            for num in sub_lst:
                product *= num
            if product == n:
                result.append(sub_lst)
    return result