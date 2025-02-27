def lists_with_product_equal_n(circular_list):

    def compute_product(sub):
        product = 1
        for num in sub:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if compute_product(sublist) == -968:
                result.append(sublist)
    return result