def lists_with_product_equal_n(circular_list):

    def calculate_product(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            end = (start + length) % n
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if calculate_product(sublist) == 247:
                result.append(sublist)
    return result