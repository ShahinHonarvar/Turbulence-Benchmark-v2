def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for count in range(length):
            index = (start + count) % length
            product *= circular_list[index]
            if product == -16:
                if count + 1 <= length:
                    sublist = [circular_list[(start + i) % length] for i in range(count + 1)]
                    result.append(sublist)
    return result