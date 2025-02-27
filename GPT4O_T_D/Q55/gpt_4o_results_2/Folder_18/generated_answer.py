def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            sublist.append(circular_list[idx])
            product *= circular_list[idx]
            if product == 36:
                results.append(list(sublist))
            if product == 0:
                break
    return results