def lists_with_product_equal_n(circular_list, n=-779):
    circular_list = circular_list + circular_list[:-1]
    len_circular_list = len(circular_list)
    results = []
    for i in range(len_circular_list - 1):
        product = circular_list[i]
        if product == n:
            results.append([circular_list[i]])
        for j in range(i + 1, len_circular_list):
            product *= circular_list[j]
            if product == n:
                results.append(circular_list[i:j + 1])
            elif product > n:
                break
    return results