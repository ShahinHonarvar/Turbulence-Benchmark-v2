def lists_with_product_equal_n(lst):

    def get_product(s):
        product = 1
        for num in s:
            product *= num
        return product
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if get_product(lst[i:j]) == -15:
                res.append(lst[i:j])
    result = []
    for item in res:
        if item not in result:
            result.append(item)
    return result