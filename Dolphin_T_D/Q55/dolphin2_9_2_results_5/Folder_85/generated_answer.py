def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist = circular_list[i:i + length]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                result.append(list(sublist))
    return result