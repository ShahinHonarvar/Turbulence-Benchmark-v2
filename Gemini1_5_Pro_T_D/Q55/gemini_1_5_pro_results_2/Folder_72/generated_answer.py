def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 10:
                result.append(sublist)
            if i != 0 and j == n - 1:
                sublist = circular_list[i:] + circular_list[:j - n + 1]
                product = 1
                for num in sublist:
                    product *= num
                if product == 10:
                    result.append(sublist)
    return result