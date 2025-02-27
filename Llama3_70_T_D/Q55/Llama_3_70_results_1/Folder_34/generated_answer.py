def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for length in range(1, n + 1):
        product = 1
        sublists = [lst[i:i + length] for i in range(n - length + 1)]
        sublists.extend([lst[i:] + lst[:length - i] for i in range(1, length)])
        for sublist in sublists:
            product = 1
            for num in sublist:
                product *= num
            if product == -81:
                result.append(sublist)
    return result