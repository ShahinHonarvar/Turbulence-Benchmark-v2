def lists_with_product_equal_n(circular_list):
    n = 15
    results = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        sublist = []
        for j in range(length):
            index = (i + j) % length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                results.append(sublist.copy())
            elif product > n:
                break
    return results