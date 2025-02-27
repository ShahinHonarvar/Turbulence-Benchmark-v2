def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(size):
            element = circular_list[(j + i) % size]
            product *= element
            sublist.append(element)
            if product == 36:
                result.append(sublist[:])
            elif product > 36:
                break
        product = 1
        sublist = []
    return result