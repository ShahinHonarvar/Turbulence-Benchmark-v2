def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    for i in range(size):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, size):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == -56:
                return [sublist]
            elif product > -56:
                break
    return []