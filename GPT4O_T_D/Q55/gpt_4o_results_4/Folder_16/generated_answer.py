def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(lst)
    lst = lst + lst[:-1]
    target_product = -837
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = lst[start:end]
            if product(sublist) == target_product:
                result.append(sublist[:n])
    return result