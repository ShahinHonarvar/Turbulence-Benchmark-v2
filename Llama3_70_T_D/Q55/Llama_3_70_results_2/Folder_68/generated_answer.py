def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            index = (i + j) % len(lst)
            product *= lst[index]
            if product == 6:
                result.append(lst[index - j:index + 1])
            elif product > 6:
                break
    return result