def lists_with_product_equal_n(circular_list):
    n = 990
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if i == 0 and j == len(circular_list) - 1:
                sublist = circular_list[:]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result