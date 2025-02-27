def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == -76:
                result.append(lst[i:i + j + 1])
                result.append(lst[(i + j + 1) % length:] + lst[:i + 1])
    return [elem for ind, elem in enumerate(result) if elem not in result[:ind]]