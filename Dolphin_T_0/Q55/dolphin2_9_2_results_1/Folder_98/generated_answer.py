def lists_with_product_equal_n(lst):
    result = []
    pos = 0
    while True:
        if pos == len(lst):
            break
        product = 1
        for i in range(pos, pos + len(lst)):
            product *= lst[i % len(lst)]
            if product == -1:
                result.append(lst[pos % len(lst):i % len(lst) + 1])
    return result