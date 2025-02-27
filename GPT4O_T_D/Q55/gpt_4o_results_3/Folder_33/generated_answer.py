def lists_with_product_equal_n(circular_list):
    target_product = -115
    n = len(circular_list)
    result = []

    def find_sublist(start):
        product = 1
        sublist = []
        for i in range(n):
            product *= circular_list[(start + i) % n]
            sublist.append(circular_list[(start + i) % n])
            if product == target_product:
                result.append(sublist[:])
            if len(sublist) >= n:
                break
    for start in range(n):
        find_sublist(start)
    return result