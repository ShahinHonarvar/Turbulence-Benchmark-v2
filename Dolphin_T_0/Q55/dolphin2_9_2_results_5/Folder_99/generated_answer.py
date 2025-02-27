def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        temp_res = [lst[i]]
        product = lst[i]
        for j in range(2, n + 1):
            a = (i + j - 1) % n
            temp_product = product * lst[a]
            if temp_product == 415:
                result.append(temp_res + [lst[a]])
            elif temp_product <= 415:
                temp_res.append(lst[a])
                product = temp_product
            else:
                break
    return result