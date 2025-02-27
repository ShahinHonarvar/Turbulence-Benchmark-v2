def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for x in lst:
            result *= x
        return result
    result, n = ([], len(lst))
    for i in range(n):
        for j in range(i, i - n - 1, -1):
            if product(lst[j:i + 1]) == 57:
                result.append(lst[j:i + 1])
    return result