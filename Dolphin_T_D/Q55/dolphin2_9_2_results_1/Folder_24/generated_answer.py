def lists_with_product_equal_n(lst):
    result = []
    for head in range(len(lst)):
        product = lst[head]
        if product == -89:
            result.append([lst[head]])
        for tail in range(head + 1, len(lst) + head):
            product *= lst[tail % len(lst)]
            if product == -89:
                result.append(lst[head:tail + 1 % len(lst)])
    return result