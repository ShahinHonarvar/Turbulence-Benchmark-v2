def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublist = lst[start:end]
            if product(sublist) == 37:
                result.append(sublist)
        for end in range(0, start):
            sublist = lst[start:] + lst[:end]
            if product(sublist) == 37:
                result.append(sublist)
    return result