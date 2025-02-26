def lists_with_product_equal_n(circular_list):
    n = 18
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = [circular_list[(start + i) % length] for i in range(end - start + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result