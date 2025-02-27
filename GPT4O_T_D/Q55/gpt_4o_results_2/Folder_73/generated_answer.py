def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            if product == 40:
                sublist = []
                for j in range(i + 1):
                    sublist.append(circular_list[(start + j) % n])
                result.append(sublist)
            if product == 0 or product > 40:
                break
    return result