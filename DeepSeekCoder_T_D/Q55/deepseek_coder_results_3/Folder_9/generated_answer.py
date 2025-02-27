def lists_with_product_equal_n(circular_list):
    n = -36
    result = []
    list_size = len(circular_list)

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    for start in range(list_size):
        for end in range(start + 1, start + list_size + 1):
            sublist = circular_list[start:end] if end <= list_size else circular_list[start:] + circular_list[:end - list_size]
            if product(sublist) == n:
                result.append(sublist)
    return result