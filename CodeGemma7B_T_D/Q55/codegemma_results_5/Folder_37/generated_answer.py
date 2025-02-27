def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        temp = [circular_list[i]]
        for j in range(1, len(circular_list)):
            next_idx = (i + j) % len(circular_list)
            product *= circular_list[next_idx]
            temp.append(circular_list[next_idx])
            if product == -76:
                result.append(temp[:])
                temp = []
                product = 1
            elif product > -76:
                temp = []
                product = 1
    return result