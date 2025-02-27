def lists_with_product_equal_n(lst):
    results = []
    head = 0
    tail = 0
    product = 1
    while tail < len(lst):
        product *= lst[tail]
        if product == 15:
            results.append(lst[head:tail + 1])
            head = tail + 1
            product = 1
        if tail == len(lst) - 1:
            tail = 0
        else:
            tail += 1
    return results