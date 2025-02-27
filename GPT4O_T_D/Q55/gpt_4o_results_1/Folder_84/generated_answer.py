def lists_with_product_equal_n(circular_list):
    target_product = -906
    n = len(circular_list)
    result = []

    def find_sublists(start, end, product, path):
        if product == target_product:
            result.append(path[:])
        if end - start == n:
            return
        next_index = end % n
        product *= circular_list[next_index]
        path.append(circular_list[next_index])
        find_sublists(start, end + 1, product, path)
        path.pop()
    for i in range(n):
        find_sublists(i, i, 1, [])
    return result