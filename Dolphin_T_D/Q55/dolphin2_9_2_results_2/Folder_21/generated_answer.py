def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    power = [1]
    for i in range(n):
        product *= lst[i]
        power.append(power[-1] * lst[i])
    for i in range(n):
        for j in range(i + 1, n + 1):
            if product == 851 and i != 0:
                result.append(lst[i:j])
            if j == n:
                return result
            product /= power[j]
    return result