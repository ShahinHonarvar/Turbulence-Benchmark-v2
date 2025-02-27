def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            if j > n:
                break
            if i + j <= n:
                sublist = circular_list[i:i + j]
            else:
                sublist = circular_list[i:] + circular_list[:i + j - n]
            if product_of_list(sublist) == -91:
                result.append(sublist)
    return result