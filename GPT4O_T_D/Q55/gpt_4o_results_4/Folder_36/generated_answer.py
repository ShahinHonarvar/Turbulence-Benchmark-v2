def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == 714:
                results.append([circular_list[(i + k) % n] for k in range(j + 1)])
            elif product > 714:
                break
    return results