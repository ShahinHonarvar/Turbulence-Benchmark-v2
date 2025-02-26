def lists_with_product_equal_n(circular_list):
    n = 51
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, i + length):
            current_sublist = []
            current_product = 1
            for k in range(i, j + 1):
                index = k % length
                current_sublist.append(circular_list[index])
                current_product *= circular_list[index]
                if current_product == n:
                    result.append(current_sublist.copy())
                    break
                if current_product > n:
                    break
    return result