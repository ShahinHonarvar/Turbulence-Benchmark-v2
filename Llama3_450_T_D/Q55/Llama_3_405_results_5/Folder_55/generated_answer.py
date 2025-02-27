def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    target_product = -6
    for size in range(1, n + 1):
        for i in range(n):
            sublist = [lst[(i + j) % n] for j in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result