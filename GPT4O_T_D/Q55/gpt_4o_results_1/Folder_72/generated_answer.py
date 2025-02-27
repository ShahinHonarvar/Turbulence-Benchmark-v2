def lists_with_product_equal_n(circular_list):

    def calculate_product(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > n:
                sublist = circular_list[start:] + circular_list[:end % n]
            else:
                sublist = circular_list[start:end]
            product = calculate_product(sublist)
            if product == 10:
                results.append(sublist)
            if end % n == start:
                break
    return results