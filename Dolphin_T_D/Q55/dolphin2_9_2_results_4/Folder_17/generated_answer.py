def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == 18:
                sublist = [circular_list[j % n] for j in range(i, i + n) if j % n != 0]
                sublists.append(sublist)
    return sublists