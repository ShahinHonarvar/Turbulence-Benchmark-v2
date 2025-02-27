def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 990:
                result.append(lst[(i + j) % n])
            elif product > 990:
                break
    return [lst[i:j] for i in range(n) for j in range(i + 1, n + 1) if eval('*'.join(map(str, lst[i:j]))) == 990]