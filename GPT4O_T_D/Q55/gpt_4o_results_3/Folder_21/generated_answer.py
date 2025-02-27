def lists_with_product_equal_n(circular_list):
    target_product = 851
    length = len(circular_list)
    result = []
    for start in range(length):
        current_product = 1
        for offset in range(length):
            index = (start + offset) % length
            current_product *= circular_list[index]
            if current_product == target_product:
                if offset + 1 <= length:
                    sublist = [circular_list[(start + i) % length] for i in range(offset + 1)]
                    result.append(sublist)
            elif current_product > target_product:
                break
    return result