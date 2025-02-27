def lists_with_product_equal_n(n):
    result = []
    for i in range(len(n)):
        product = 1
        if n[i] == -15:
            result.append([n[i]])
        for j in range(i, len(n)):
            product *= n[(j + i) % len(n)]
            if i != j and product == -15:
                result.append(n[i:j + 1])
            elif product > -15:
                break
    return result