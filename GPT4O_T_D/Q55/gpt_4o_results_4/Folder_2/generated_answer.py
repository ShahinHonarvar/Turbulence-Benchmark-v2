def lists_with_product_equal_n(circular_list):
    target = -968
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(start, start + n):
            index = end % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == target:
                result.append(sublist[:])
            if abs(product) > abs(target) or product == 0:
                break
    return result