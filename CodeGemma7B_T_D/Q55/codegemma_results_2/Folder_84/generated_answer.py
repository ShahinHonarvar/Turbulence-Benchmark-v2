def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        j = i + 1
        while j != i:
            if product * circular_list[j] == -906:
                result.append([circular_list[k] for k in range(i, j + 1)])
            if product * circular_list[j] == 1:
                break
            j = (j + 1) % len(circular_list)
            product *= circular_list[j]
    return result