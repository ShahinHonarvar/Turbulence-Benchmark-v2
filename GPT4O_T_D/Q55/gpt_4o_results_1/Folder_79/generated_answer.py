def lists_with_product_equal_n(circular_list):
    target_product = -83
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            current_index = (start + end) % n
            product *= circular_list[current_index]
            if product == target_product:
                sublist = []
                for i in range(end + 1):
                    sublist.append(circular_list[(start + i) % n])
                results.append(sublist)
            if product == 0:
                break
    return results