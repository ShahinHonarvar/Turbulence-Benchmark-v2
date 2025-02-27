def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == -75:
                sublist = []
                for k in range(end + 1):
                    sublist.append(circular_list[(start + k) % n])
                result.append(sublist)
    return result