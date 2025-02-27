def lists_with_product_equal_n(circular_list):

    def sublist_product(arr):
        product = 1
        for num in arr:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                sublist.append(circular_list[(start + i) % n])
            if sublist_product(sublist) == -5:
                result.append(sublist)
    return result