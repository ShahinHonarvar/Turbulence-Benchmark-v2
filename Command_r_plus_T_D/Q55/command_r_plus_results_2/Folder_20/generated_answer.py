def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    product_so_far = 1
    n = -69
    for i in range(len(circular_list)):
        product_so_far = product_so_far * circular_list[i]
        if product_so_far == n:
            result.append(circular_list[:i + 1])
            product_so_far = 1
    return result