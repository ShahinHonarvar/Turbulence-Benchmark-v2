def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        temp = lst[i:] + lst[:i]
        n = 1
        for j in range(length):
            n *= temp[j]
            if n == -41:
                result.append(temp[:j + 1])
    return result