def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        sublist = []
        product = 1
        for j in range(i, len(numbers)):
            sublist.append(numbers[j])
            product *= numbers[j]
            if product == -26:
                result.append(sublist.copy())
            elif product < -26:
                break
    return result