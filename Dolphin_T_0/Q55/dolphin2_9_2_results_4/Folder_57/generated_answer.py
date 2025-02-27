def product_equal_n(lst, n):
    product_list = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i:j + 1] not in product_list and i != j) and (lst[j:] + lst[:i] not in product_list and i != j):
                product = 1
                for k in lst[i:j + 1]:
                    product *= k
                if product == n:
                    product_list.append(lst[i:j + 1])
    return product_list