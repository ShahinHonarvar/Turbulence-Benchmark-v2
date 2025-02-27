def lists_with_product_equal_n(circ_list):
    n = 43
    size = len(circ_list)
    circ_list *= 2
    results = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circ_list[end]
            if product == n:
                results.append(circ_list[start:end + 1])
            elif product > n:
                break
    return results