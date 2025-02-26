def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [lst[(start + i) % n] for i in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == -82:
                result.append(sublist)
    return result