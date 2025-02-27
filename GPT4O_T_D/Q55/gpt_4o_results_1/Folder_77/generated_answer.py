def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 632:
                result.append(sublist[:])
            if product == 0:
                break
            if product > 632:
                while product > 632 and sublist:
                    product //= sublist.pop(0)
                    if product == 632:
                        result.append(sublist[:])
    return result