def lists_with_product_equal_n(circular_list):

    def product(sublist):
        res = 1
        for num in sublist:
            res *= num
        return res
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > n:
                end %= n
                sublist = circular_list[start:] + circular_list[:end]
            else:
                sublist = circular_list[start:end] if end > start else circular_list[start:n] + circular_list[:end]
            if product(sublist) == -1:
                result.append(sublist)
    return result