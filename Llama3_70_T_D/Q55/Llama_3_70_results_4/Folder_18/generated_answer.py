def lists_with_product_equal_n(lst):

    def is_product_n(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > 36:
                return False
        return product == 36
    result = set()
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, i + n):
            if j - i <= n:
                sublist = lst[i:j]
                if is_product_n(sublist):
                    result.add(tuple(sublist))
    return [list(sublist) for sublist in result]