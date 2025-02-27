def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if product(sublist) == 4:
                result.append(sublist)
        if i < n - 1:
            for j in range(0, i + 1):
                sublist = lst[i:] + lst[:j]
                if product(sublist) == 4:
                    result.append(sublist)
    return result