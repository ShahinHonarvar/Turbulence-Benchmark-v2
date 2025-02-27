def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    size = len(circular_list)
    result = []
    for start in range(size):
        for end in range(1, size + 1):
            if end > size or start + end < size:
                sublist = circular_list[start:start + end]
            else:
                sublist = circular_list[start:] + circular_list[:start + end - size]
            if product(sublist) == 78:
                result.append(sublist)
    return result