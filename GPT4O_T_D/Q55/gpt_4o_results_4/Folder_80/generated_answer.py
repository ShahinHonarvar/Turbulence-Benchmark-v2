def lists_with_product_equal_n(circular_list):
    target_product = 43
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == target_product:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            if product == 0 or product > target_product:
                break
    return result