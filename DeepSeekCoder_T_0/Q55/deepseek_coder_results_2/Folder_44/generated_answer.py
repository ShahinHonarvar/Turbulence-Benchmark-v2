def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = 29
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start + 1, start + length + 1):
            sublist = circular_list[start:end] if end <= length else circular_list[start:] + circular_list[:end - length]
            if product(sublist) == n:
                result.append(sublist)
    return result