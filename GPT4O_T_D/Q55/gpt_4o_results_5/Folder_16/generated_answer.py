def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if end > start + n:
                break
            sublist = [circular_list[i % n] for i in range(start, end)]
            if product(sublist) == -837:
                result.append(sublist)
    return result