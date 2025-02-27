def lists_with_product_equal_n(l, n=-22):
    result = []
    length = len(l)
    for i in range(length):
        for j in range(i + 1, length + 1):
            product = 1
            for k in range(i, j):
                product *= l[k % length]
            if product == n:
                result.append(l[i:j])
    return result