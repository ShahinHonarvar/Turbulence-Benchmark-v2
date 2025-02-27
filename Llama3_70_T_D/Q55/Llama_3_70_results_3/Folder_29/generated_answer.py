def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = lst[i:j % n + 1]
            if product(sublist) == 15:
                result.append(sublist)
    return result