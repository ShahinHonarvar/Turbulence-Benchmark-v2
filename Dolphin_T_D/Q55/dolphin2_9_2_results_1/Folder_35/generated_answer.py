def lists_with_product_equal_n(lst):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if size < n:
                sublist.append(lst[0])
            if get_product(sublist) == 83:
                result.append(sublist)
    return result