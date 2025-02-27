def list_with_product_equal_n(lst):
    prod_n = 1
    for i in lst:
        prod_n *= i
    if prod_n != 28:
        return []
    n = len(lst)
    lst_cycle = [lst[i % n] for i in range(n * 2)]
    result = []
    for i in range(n * 2):
        product = 1
        for j in range(i, i + n):
            product *= lst_cycle[j]
            if product == 28:
                temp_list = []
                for k in range(i, j + 1):
                    temp_list.append(lst_cycle[k % n])
                result.append(temp_list)
    return result