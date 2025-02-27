def lists_with_product_equal_n(circular_list):

    def calculate_product(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if calculate_product(sublist) == 537:
                result.append(sublist)
    return result