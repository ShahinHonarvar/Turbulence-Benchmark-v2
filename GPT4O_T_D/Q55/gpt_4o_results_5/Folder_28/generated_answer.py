def lists_with_product_equal_n(circular_list):
    target_product = 85
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(1, n + 1):
            product = 1
            sublist = []
            for k in range(end):
                index = (start + k) % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
                if product == target_product:
                    result.append(list(sublist))
    return result