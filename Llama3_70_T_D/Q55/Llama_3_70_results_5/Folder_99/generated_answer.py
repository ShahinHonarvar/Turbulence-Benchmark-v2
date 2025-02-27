def lists_with_product_equal_n(lst):

    def is_valid(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 415
    n = len(lst)
    result = set()
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = lst[i:j]
            if is_valid(sublist):
                result.add(tuple(sorted(sublist)))
    return [list(sublist) for sublist in result]