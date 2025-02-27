def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == 74:
                result.append(lst[index - j:index] if index - j >= 0 else lst[index - j:] + lst[:index])
            elif product > 74:
                break
    return result