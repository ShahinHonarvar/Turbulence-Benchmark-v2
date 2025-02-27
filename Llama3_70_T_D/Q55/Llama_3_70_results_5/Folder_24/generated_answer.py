def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            index = (i + j) % length
            product *= lst[index]
            if product == -89:
                result.append(lst[index - j:index + 1])
    return result