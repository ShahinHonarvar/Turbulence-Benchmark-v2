def lists_with_product_equal_n(circular_list):

    def sublists_with_product_product(arr, start, length, target):
        sublists = []
        product = 1
        for i in range(length):
            product *= arr[(start + i) % length]
            if product == target:
                sublists.append([arr[(start + j) % length] for j in range(i + 1)])
        return sublists
    n = len(circular_list)
    result = []
    for start in range(n):
        result.extend(sublists_with_product_product(circular_list, start, n, 28))
    return result