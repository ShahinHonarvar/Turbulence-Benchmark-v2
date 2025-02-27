def lists_with_product_equal_n(circular_list):
    sublists = []
    n = -95
    length = len(circular_list)
    circular_list += circular_list
    for i in range(length):
        for j in range(i + 1, 2 * length):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
                if product == n:
                    sublists.append(circular_list[i:j])
            if product < n:
                break
    return sublists