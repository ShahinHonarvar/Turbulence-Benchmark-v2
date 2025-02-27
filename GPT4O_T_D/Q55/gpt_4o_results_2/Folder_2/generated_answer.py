def lists_with_product_equal_n(circular_list):
    target_product = -968
    n = len(circular_list)
    result = []

    def find_product(start, end):
        product = 1
        while True:
            product *= circular_list[end % n]
            if product == target_product:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            if end - start + 1 == n:
                break
            end += 1
    for i in range(n):
        find_product(i, i)
    return result