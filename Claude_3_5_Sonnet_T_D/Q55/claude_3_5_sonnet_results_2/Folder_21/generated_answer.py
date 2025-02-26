def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            product = 1
            for num in sublist:
                product *= num
                if product > 851:
                    break
            if product == 851:
                result.append(sublist)
    return result