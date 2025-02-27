def lists_with_product_equal_n(circular_list):

    def find_sublists(start, end, n):
        product = 1
        sublists = []
        for i in range(end):
            product *= circular_list[(start + i) % n]
            if product == 10:
                sublists.append([circular_list[(start + j) % n] for j in range(i + 1)])
            if product == 0:
                break
        return sublists
    n = len(circular_list)
    result = []
    for start in range(n):
        result.extend(find_sublists(start, n, n))
    return result