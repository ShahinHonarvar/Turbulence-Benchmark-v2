def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 27:
                result.append(lst[(i + j) % n])
            elif product > 27:
                break
    return [lst[i:j] for i in range(n) for j in range(i + 1, n + 1) if len(lst[i:j]) <= n and eval('*'.join(map(str, lst[i:j]))) == 27]