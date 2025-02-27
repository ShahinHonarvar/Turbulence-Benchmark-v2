def lists_with_product_equal_n(circular_list):

    def product(sublist):
        prod = 1
        for number in sublist:
            prod *= number
        return prod
    n = -6
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            if start + end > length:
                sublist = circular_list[start:] + circular_list[:(start + end) % length]
            else:
                sublist = circular_list[start:start + end]
            if product(sublist) == n:
                result.append(sublist)
    return result