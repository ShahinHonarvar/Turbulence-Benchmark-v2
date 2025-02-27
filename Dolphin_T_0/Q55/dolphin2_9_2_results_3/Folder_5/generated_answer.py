def lists_with_product_equal_n(lst):

    def multiply_list(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    results = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            spl = lst[i:j]
            if len(spl) < size:
                spl = spl + lst[:len(spl)]
            if multiply_list(spl) == -33:
                results.append(spl)
    return results