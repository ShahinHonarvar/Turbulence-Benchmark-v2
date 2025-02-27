def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 733:
                result.append(lst[(i + j) % len(lst):] + lst[:i])
                break
            elif product > 733:
                break
    return result