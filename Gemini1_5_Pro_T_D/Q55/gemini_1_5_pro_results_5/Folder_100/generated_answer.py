def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 48:
                result.append(sublist)
            if j - i + 1 == n:
                break
    return result