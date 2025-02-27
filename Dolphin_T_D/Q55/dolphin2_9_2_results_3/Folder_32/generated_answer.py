def lists_with_product_equal_n(lst):

    def product(l):
        result = 1
        for i in l:
            result *= i
        return result
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if product(lst[i:j]) == 76:
                result.append(lst[i:j])
    return result