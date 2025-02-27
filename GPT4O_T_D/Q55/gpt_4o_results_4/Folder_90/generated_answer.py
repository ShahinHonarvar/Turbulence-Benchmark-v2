def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []

    def contiguous_product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = [circular_list[i % n] for i in range(start, end)]
            if contiguous_product(sublist) == -690:
                results.append(sublist)
    return results