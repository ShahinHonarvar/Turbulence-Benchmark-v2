def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = 25
    length = len(circular_list)
    result = []
    for start in range(length):
        for size in range(1, length + 1):
            if start + size <= length:
                sublist = circular_list[start:start + size]
            else:
                sublist = circular_list[start:] + circular_list[:(start + size) % length]
            if product(sublist) == n:
                result.append(sublist)
    return result