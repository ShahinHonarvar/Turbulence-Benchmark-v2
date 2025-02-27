def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        j = i + 1
        product = circular_list[i]
        sublist = [circular_list[i]]
        while j % len(circular_list) != i:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j = j + 1
            if product == -91:
                return sublist
            elif product > -91:
                break
    return []