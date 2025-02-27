def lists_with_product_equal_n(lst):
    result = []
    for length in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            for j in range(length):
                product *= lst[(i + j) % len(lst)]
            if product == 78:
                result.append(lst[i:i + length])
    return result