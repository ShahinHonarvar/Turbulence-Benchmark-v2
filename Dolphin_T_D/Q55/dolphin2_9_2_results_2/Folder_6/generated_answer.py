def lists_with_product_equal_n(lst):

    def get_product(lst):
        product = 1
        for number in lst:
            product *= number
        return product
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if get_product(sublist) == 42:
                result.append(sublist)
    return result