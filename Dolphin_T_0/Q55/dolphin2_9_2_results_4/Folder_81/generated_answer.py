def lists_with_product_equal_n(numbers, n=-8):
    result = []
    product_so_far = 1
    indexes = []
    for i in range(len(numbers)):
        product_so_far *= numbers[i]
        indexes.append(i)
        if product_so_far % n == 0:
            for j in range(1, len(indexes) + 1):
                result.append(numbers[i - j + 1:i + 1])
    return result if result else []