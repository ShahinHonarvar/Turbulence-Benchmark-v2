def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n + i):
            sublist = lst[j % n:] + lst[:j % n]
            for k in range(len(sublist)):
                if product(sublist[:k + 1]) == 33 and sublist[:k + 1] not in result:
                    result.append(sublist[:k + 1])
    return result