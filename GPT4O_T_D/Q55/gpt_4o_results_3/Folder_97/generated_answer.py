def lists_with_product_equal_n(lst):
    n = len(lst)
    target_product = -938
    result = []

    def find_product(sublst):
        product = 1
        for num in sublst:
            product *= num
        return product
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                sublist.append(lst[(start + i) % n])
            if find_product(sublist) == target_product:
                result.append(sublist)
    return result