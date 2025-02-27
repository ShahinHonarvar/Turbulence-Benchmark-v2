def lists_with_product_equal_n(numbers):
    result = []
    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
        if product == 0:
            result.append(numbers[:i + 1])
    return result