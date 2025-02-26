def lists_with_product_equal_n(circular_list):
    n = 27
    result = []
    length = len(circular_list)
    extended_list = circular_list * 2
    for start in range(length):
        for end in range(start, start + length):
            sublist = extended_list[start:end + 1]
            product = 1
            for num in sublist:
                product *= num
                if product > n:
                    break
            if product == n:
                result.append(sublist)
    return result