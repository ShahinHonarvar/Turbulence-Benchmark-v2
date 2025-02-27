def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 49:
                result.append(lst[(i + j) % len(lst)])
            elif product > 49:
                break
    result2 = []
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] == result[j]:
                result2.append(result[i])
                break
    return result + result2