def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = -20
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if product(sublist) == n:
                result.append(sublist)
            if i != 0 and j == len(lst):
                sublist = lst[i:] + lst[:i]
                if product(sublist) == n:
                    result.append(sublist)
    return result