def lists_with_product_equal_n(lst):
    result = []
    head = 0
    for tail in range(0, len(lst)):
        prod = 1
        for i in range(head, tail + 1):
            prod *= lst[i % len(lst)]
            if prod == 15:
                result.append(lst[head % len(lst):tail % len(lst) + 1])
    return result