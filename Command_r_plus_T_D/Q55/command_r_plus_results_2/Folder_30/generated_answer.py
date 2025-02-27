def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    product = 1
    n = 99
    for i in range(len(circular_list)):
        product = product * circular_list[i]
        if product == n:
            result.append(circular_list[:i + 1])
            product = 1
        if product > n:
            product = 1
    return result