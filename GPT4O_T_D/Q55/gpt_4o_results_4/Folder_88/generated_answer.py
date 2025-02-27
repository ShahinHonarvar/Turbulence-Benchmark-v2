def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)

    def find_sublist(start, end):
        sublist = []
        product = 1
        index = start
        for _ in range(end):
            product *= circular_list[index]
            sublist.append(circular_list[index])
            index = (index + 1) % n
        return (product, sublist)
    for size in range(1, n + 1):
        for start in range(n):
            product, sublist = find_sublist(start, size)
            if product == -56:
                result.append(sublist)
    return result