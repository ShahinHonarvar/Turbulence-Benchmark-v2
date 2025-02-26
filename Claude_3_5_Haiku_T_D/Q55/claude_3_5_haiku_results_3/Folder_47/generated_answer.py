def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [arr[(start + i) % n] for i in range(length)]
            product = 1
            for num in sublist:
                product *= num
            if product == -94:
                result.append(sublist)
    return result