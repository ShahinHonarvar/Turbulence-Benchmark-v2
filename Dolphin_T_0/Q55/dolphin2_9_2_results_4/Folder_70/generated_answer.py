def lists_with_product_equal_n(lst, n=32):
    lst = lst + lst
    res = []
    for start in range(len(lst) - 1):
        for end in range(start + 1, len(lst)):
            sub_lst = lst[start:end + 1]
            if sub_lst[-1] == sub_lst[0] and len(set(sub_lst)) != len(sub_lst):
                product = 1
                for num in sub_lst:
                    product *= num
                if product == n:
                    res.append(list(sub_lst))
    return res