def lists_with_product_equal_n(lst):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    n = len(lst)
    for length in range(1, n + 1):
        for i in range(n):
            sublist = [lst[(i + j) % n] for j in range(length)]
            if get_product(sublist) == -9:
                result.append(sublist)
    return result