def lists_with_product_equal_n(circular_list, n):
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i + 1, length + 1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                result.append(sublist)
    return result