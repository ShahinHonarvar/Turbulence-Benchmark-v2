def lists_with_product_equal_n(circular_list):

    def sublists_with_product(start, end, target):
        sublists = []
        product = 1
        length = len(circular_list)
        for i in range(end - start + 1):
            product *= circular_list[(start + i) % length]
            if product == target:
                sublists.append([circular_list[(start + j) % length] for j in range(i + 1)])
            if product > target or (i < end - start and product == 0):
                break
        return sublists
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(start, start + n):
            result.extend(sublists_with_product(start, end, 10))
    return result