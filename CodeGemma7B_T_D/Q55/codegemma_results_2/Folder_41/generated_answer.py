def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        j = i + 1
        product = circular_list[i]
        sublist = [circular_list[i]]
        while j < len(circular_list) or (j == 0 and circular_list[i] * circular_list[j] == -20):
            if j >= len(circular_list):
                j = 0
            if circular_list[i] * circular_list[j] == -20:
                product *= circular_list[j]
                sublist.append(circular_list[j])
                j += 1
            elif product == -20:
                return [sublist]
            else:
                break
    return []