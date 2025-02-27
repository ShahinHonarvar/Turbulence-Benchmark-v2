def lists_with_product_equal_n(circular_list):
    target_product = 851
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        length = 0
        for i in range(n):
            current_product *= circular_list[(start + i) % n]
            length += 1
            if length > n:
                break
            if current_product == target_product:
                sublist = [circular_list[(start + j) % n] for j in range(length)]
                result.append(sublist)
                break
            if current_product > target_product:
                break
    return result