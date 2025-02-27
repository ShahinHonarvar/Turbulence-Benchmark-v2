def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 49:
                results.append(sublist[:])
            elif product > 49 or i == n - 1:
                break
    return results