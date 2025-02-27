def lists_with_product_equal_n(n, circular_list):
    sublists = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sub = circular_list[i:j]
            sub.extend(circular_list[0:i])
            product = 1
            for k in range(0, size):
                product *= sub[k]
            if product == n:
                sublists.append(sub)
    return sublists