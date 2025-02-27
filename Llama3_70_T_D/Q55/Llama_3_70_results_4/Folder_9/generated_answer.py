def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -36:
                result.append(lst[(i + j) % len(lst)])
                break
            elif product > -36:
                break
    return [lst[i:j + 1] for i, j in [(i, i + result.count(x) - 1) for i, x in enumerate(result)]]