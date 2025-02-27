def lists_with_product_equal_n(lst):
    result = []
    start = 0
    while True:
        end = start + 1
        product = 1
        while end != start:
            product *= lst[start]
            if product == 10:
                result.append(lst[start:end])
            product *= lst[start]
            end += 1
            if end == len(lst):
                end = 0
            if end == start:
                break
        start += 1
        if start == len(lst):
            break
    return result