def lists_with_product_equal_n(lst):
    result = []
    start = 0
    end = 1
    product = lst[0]
    while product != -968:
        while end < len(lst):
            product *= lst[end]
            if product > -968 or end - start + 1 > len(lst):
                start += 1
                product = lst[start]
                end = start + 1
            elif product == -968:
                result.append(lst[start:end + 1])
                start += 1
                product = lst[start]
                end = start + 1
        start = 0
        end = 1
        product = lst[0]
    return result