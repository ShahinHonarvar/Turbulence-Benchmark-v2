def lists_with_product_equal_n(circular_list):
    n = 32
    result = []
    list_len = len(circular_list)
    for size in range(1, list_len + 1):
        for start in range(list_len):
            sublist = [circular_list[(start + i) % list_len] for i in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result