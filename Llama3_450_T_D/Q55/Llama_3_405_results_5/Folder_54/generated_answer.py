def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if product(sublist) == -17:
                result.append(sublist)
            if i == 0 and j == n:
                break
            if j == n:
                sublist = lst[i:] + lst[:j - n]
                if product(sublist) == -17:
                    result.append(sublist)
    return result