def lists_with_product_equal_n(circular_list):
    results = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 90:
                results.append(list(sublist))
            if product == 0 or product > 90:
                break
    return results