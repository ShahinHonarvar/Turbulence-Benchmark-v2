def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= lst[index]
            if product == 43:
                result.append(lst[index - j:index] + lst[:index] if index > j else lst[index - j:index + 1])
            elif product > 43:
                break
    return result