def lists_with_product_equal_n(circular_list):
    n = 415
    length = len(circular_list)
    results = []

    def product_of_sublist(start, end):
        product = 1
        for i in range(start, end + 1):
            index = i % length
            product *= circular_list[index]
        return product
    for i in range(length):
        for size in range(1, length + 1):
            if i + size > i + length:
                break
            if product_of_sublist(i, i + size - 1) == n:
                sublist = [circular_list[j % length] for j in range(i, i + size)]
                results.append(sublist)
    return results