def lists_with_product_equal_n(circular_list):
    n = 28
    result = []
    list_size = len(circular_list)
    for size in range(1, list_size + 1):
        for i in range(list_size):
            sublist = [circular_list[(i + j) % list_size] for j in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result