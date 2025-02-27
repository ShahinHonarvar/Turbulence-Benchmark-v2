def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == -54:
                result.append(lst[(i + j) % length])
                break
            elif product > -54:
                break
    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1) if lst[i:j] in result]