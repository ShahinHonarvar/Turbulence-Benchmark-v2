def lists_with_product_equal_n(circular_list):

    def product_of_list(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        current_product = 1
        for offset in range(n):
            current_index = (start + offset) % n
            current_product *= circular_list[current_index]
            if current_product == -6:
                sublist = [circular_list[(start + i) % n] for i in range(offset + 1)]
                results.append(sublist)
    return results