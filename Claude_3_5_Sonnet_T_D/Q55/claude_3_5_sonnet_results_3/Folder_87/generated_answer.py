def lists_with_product_equal_n(circular_list):
    n = 27
    result = []
    length = len(circular_list)
    for start in range(length):
        for size in range(1, length + 1):
            sublist = []
            product = 1
            for i in range(size):
                index = (start + i) % length
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product > n:
                    break
            if product == n:
                result.append(sublist)
    return result