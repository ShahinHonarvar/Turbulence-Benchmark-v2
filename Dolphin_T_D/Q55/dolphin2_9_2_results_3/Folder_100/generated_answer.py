def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    product = 1
    start = 0
    for end in range(len(lst)):
        product1 = product * lst[end]
        if product1 == 48:
            result.append(lst[start:end + 1])
        while product1 >= 48:
            product /= lst[start]
            start += 1
            if product == 1 and start != len(lst):
                product = 1
                index = end + 1
                while index % len(lst) != start:
                    product *= lst[index % len(lst)]
                    index += 1
                end = index - 1
            if start != end + 1:
                product1 = product * lst[end]
    return result