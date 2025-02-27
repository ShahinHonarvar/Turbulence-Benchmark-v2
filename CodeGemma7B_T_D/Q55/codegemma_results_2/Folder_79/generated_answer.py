def lists_with_product_equal_n(circ_list):
    multiply = -83
    output = []
    length = len(circ_list)
    for i in range(length):
        current = [circ_list[i]]
        current_product = circ_list[i]
        for j in range(1, length):
            current.append(circ_list[(i + j) % length])
            current_product *= circ_list[(i + j) % length]
            if current_product == multiply:
                output.append(current[:])
            elif current_product > multiply:
                break
    return output