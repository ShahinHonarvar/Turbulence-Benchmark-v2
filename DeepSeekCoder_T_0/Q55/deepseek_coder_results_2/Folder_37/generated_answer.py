def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target = -76
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == target:
                result.append(sublist.copy())
            if product == 0 or (product > target and circular_list[idx] != 1):
                break
        if product == target:
            for i in range(n - len(sublist)):
                idx = (start + len(sublist) + i) % n
                product *= circular_list[idx]
                sublist.append(circular_list[idx])
                if product == target:
                    result.append(sublist.copy())
                if product != target:
                    break
    return result