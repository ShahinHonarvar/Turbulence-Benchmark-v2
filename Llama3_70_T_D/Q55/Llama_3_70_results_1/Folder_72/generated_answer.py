def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(1, n + 1):
        for j in range(n):
            temp = lst[j:j + i]
            if j + i > n:
                temp += lst[:j + i - n]
            product = 1
            for k in temp:
                product *= k
            if product == 10:
                result.append(temp)
    return result