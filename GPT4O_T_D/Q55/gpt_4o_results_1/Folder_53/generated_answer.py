def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    results = []
    for start in range(length):
        for size in range(1, length + 1):
            product = 1
            sublist = []
            for i in range(size):
                idx = (start + i) % length
                sublist.append(circular_list[idx])
                product *= circular_list[idx]
            if product == -87:
                results.append(sublist)
    return results