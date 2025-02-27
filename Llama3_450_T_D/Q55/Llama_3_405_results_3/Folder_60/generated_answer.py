def lists_with_product_equal_n(circular_list):
    n = 49
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= circular_list[(i + j) % length]
            if product == n:
                result.append(circular_list[i:i + j + 1])
            elif product > n or j == length - 1:
                break
    for i in range(length):
        product = 1
        for j in range(i + 1, length + i):
            product *= circular_list[j % length]
            if product == n and j - i > 1:
                result.append(circular_list[i:j])
    return [x for i, x in enumerate(result) if x not in result[:i]]