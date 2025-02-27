def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == 33:
                length = (end - start + 1) % n
                if length == 0:
                    length = n
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            elif product == 0 or (product > 33 and product % 33 != 0):
                break
    return result