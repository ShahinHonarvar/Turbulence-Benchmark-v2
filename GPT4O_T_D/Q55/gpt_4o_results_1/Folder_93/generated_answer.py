def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    sublists = []
    for start in range(n):
        for end in range(1, n + 1):
            indices = [i % n for i in range(start, start + end)]
            sublist = [circular_list[i] for i in indices]
            if product(sublist) == -91:
                sublists.append(sublist)
    return sublists