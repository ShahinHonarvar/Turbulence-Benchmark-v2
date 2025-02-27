def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == 48:
                sublist = [circular_list[(start + i) % n] for i in range(end + 1)]
                result.append(sublist)
            if product == 0 or product > 48:
                break
    return result