def lists_with_product_equal_n(lst):

    def calc_product(sublist):
        result = 1
        for n in sublist:
            result *= n
        return result
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if calc_product(sublist) == 10:
                result.append(sublist)
    return result