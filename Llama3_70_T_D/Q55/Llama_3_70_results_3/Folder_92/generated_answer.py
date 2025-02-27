def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)

    def is_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 5
    for size in range(1, n + 1):
        for i in range(n):
            for j in range(i, i + size):
                if j >= n:
                    sublist = lst[i:] + lst[:j - n]
                else:
                    sublist = lst[i:j]
                if is_product_equal_n(sublist):
                    result.append(sublist)
    return result