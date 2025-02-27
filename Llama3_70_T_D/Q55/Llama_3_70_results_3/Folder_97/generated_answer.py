def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == -938:
                result.append(lst[(i + j) % length])
            elif product < -938:
                break
    result2 = []
    for i in range(len(result) - 1):
        if result[i + 1] != result[i]:
            result2.append(result[i])
    return [result[i:i + result2.count(result[i]) + 1] for i in range(len(result2))]