def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 100:
                results.append(sublist[:])
            elif product > 100:
                break
    return results