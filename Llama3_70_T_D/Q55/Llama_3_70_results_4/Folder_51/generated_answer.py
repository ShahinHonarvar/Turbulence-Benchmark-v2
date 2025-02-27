def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            index = (i + j) % length
            product *= lst[index]
            if product == -44:
                result.append(lst[index - j:index] if index >= j else lst[index:] + lst[:j + 1])
    return result