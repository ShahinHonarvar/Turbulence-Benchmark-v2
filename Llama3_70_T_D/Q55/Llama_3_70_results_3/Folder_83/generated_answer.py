def lists_with_product_equal_n(lst):

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -57
    result = []
    size = len(lst)
    for i in range(size):
        for j in range(i, i + size):
            sublist = lst[i:j % size + 1]
            if check_product(sublist):
                result.append(sublist)
    return result