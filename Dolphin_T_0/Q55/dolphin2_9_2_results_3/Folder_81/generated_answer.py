def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    n = len(lst)
    sublists = []
    for i in range(n):
        temp = lst[i:] + lst[:i]
        for j in range(1, n + 1):
            for k in range(j, n + 1):
                if product(temp[k - j:k]) == -8:
                    sublists.append(temp[k - j:k])
    return sublists