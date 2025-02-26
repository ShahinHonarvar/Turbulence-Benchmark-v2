def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [lst[(start + i) % n] for i in range(end - start + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == 2:
                result.append(sublist)
    return result