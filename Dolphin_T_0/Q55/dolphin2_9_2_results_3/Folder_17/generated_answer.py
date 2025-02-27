def lists_with_product_equal_n(lst):

    def get_product(arr):
        product = 1
        for i in arr:
            product *= i
        return product
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if get_product(sublist) == 18:
                result.append(sublist)
    return result