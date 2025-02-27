def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -56:
                result.append(lst[(i + j) % len(lst)])
                break
            elif product > -56:
                break
    result2 = []
    for x in result:
        if lst.count(x) > 1:
            result2.append(lst[:lst.index(x)] + [x] * lst.count(x) + lst[lst.index(x) + lst.count(x):])
    for x in result2:
        result.append(x)
    return result