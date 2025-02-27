def lists_with_product_equal_n(circular_list):
    prod = 1
    output = []
    pointer = 0
    compare = pointer + 1
    length = len(circular_list)
    while pointer < length and compare < length:
        if prod == 37:
            output.append(circular_list[pointer:compare + 1])
            pointer += 1
            compare += 1
            prod = 1
        elif prod > 37:
            pointer += 1
            compare += 1
            prod = 1
        else:
            prod *= circular_list[compare]
            compare += 1
    return output