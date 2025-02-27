def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 537:
                result.append(sublist[:])
            if product == 0 or product > 537:
                break
    return result