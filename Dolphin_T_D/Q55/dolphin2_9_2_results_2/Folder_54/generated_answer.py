def lists_with_product_equal_n(lst, n=-17):
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sub_lst = lst[i:j]
            if sub_lst != [] and j - i == 1:
                product = 1
                for k in sub_lst:
                    product *= k
                if product == n:
                    result.append(sub_lst)
            elif sub_lst != []:
                product = 1
                for k in sub_lst[:-1]:
                    product *= k
                if product == n * sub_lst[-1]:
                    result.append(sub_lst)
    return result