def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        circular_list.append(circular_list.pop(0))
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in range(j, len(circular_list)):
                product *= circular_list[k]
                if product == 90:
                    return [circular_list[i:k + 1]]
                elif product > 90:
                    break
    return []