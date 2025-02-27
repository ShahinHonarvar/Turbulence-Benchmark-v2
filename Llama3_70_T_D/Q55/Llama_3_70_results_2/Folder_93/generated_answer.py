def lists_with_product_equal_n(lst):

    def product(sublist):
        res = 1
        for num in sublist:
            res *= num
        return res
    result = []
    for start in range(len(lst)):
        for end in range(start, len(lst)):
            current_sublist = lst[start:end + 1]
            if product(current_sublist) == -91:
                result.append(current_sublist)
        for end in range(0, start):
            current_sublist = lst[start:] + lst[:end + 1]
            if product(current_sublist) == -91:
                result.append(current_sublist)
    return result