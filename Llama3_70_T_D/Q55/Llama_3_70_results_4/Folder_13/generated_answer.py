def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == 54:
                result.append(lst[index - j:index] + lst[:index - j + 1])
            elif product > 54:
                break
    return result