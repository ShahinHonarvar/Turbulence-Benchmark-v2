def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            current_sublist = [lst[(start + i) % n] for i in range(length)]
            product = 1
            for num in current_sublist:
                product *= num
            if product == 29:
                result.append(current_sublist)
    return result