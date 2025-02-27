def lists_with_product_equal_n(circular_list, n=33):
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list) + 1):
            sublist = circular_list[start:end]
            sublist += circular_list[:end - len(circular_list)]
            if sublist and sublist[0] * sublist[-1] == n:
                return [sublist]
    return []