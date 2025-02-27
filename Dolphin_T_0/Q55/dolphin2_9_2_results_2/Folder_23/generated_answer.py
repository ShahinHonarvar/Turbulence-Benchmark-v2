def lists_with_product_equal_n(lst):
    if not lst:
        return []

    def check_product(lst, n):
        product = 1
        for number in lst:
            product *= number
        return product == n
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            curr_lst = lst[i:j]
            if check_product(curr_lst, -95):
                res.append(curr_lst)
    return res