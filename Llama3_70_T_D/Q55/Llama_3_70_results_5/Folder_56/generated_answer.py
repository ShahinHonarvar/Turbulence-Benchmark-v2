def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -65:
                result.append(lst[(i + j) % n])
            elif product != -65 and j > 0 and (product % lst[(i + j) % n] == 0):
                product //= lst[(i + j) % n]
    return [lst[i:n + i] for i in range(n) if lst[i] * lst[(i + 1) % n] * lst[(i + 2) % n] == -65]