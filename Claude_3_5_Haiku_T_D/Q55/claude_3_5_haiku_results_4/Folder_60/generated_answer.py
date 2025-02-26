def lists_with_product_equal_n(circular_list):
    n = 49
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(length):
            sublist = []
            product = 1
            k = 0
            while k < length:
                current_index = (i + k) % length
                product *= circular_list[current_index]
                sublist.append(circular_list[current_index])
                if product == n:
                    result.append(sublist.copy())
                    break
                if product > n:
                    break
                k += 1
    return result