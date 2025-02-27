def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            current_indices = [(start + i) % n for i in range(end)]
            current_list = [circular_list[i] for i in current_indices]
            if product(current_list) == 5:
                result.append(current_list)
    return result