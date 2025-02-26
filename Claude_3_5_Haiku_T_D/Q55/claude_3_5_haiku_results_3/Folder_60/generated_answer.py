def lists_with_product_equal_n(circular_list):
    n = 49
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = [circular_list[(start + i) % list_length] for i in range(end - start + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result