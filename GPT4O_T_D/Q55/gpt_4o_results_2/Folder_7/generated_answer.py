def lists_with_product_equal_n(circular_list):
    target = 537
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(length):
            index = (i + j) % length
            product *= circular_list[index]
            if product == target:
                if j == length - 1:
                    result.append(circular_list[index + 1:] + circular_list[:index + 1])
                else:
                    result.append(circular_list[i:index + 1])
            elif product > target:
                break
    return result