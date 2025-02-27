def lists_with_product_equal_n(circular_list):

    def product(lst):
        res = 1
        for num in lst:
            res *= num
        return res
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            if j <= n:
                sublist = circular_list[i:i + j]
                if product(sublist) == -61:
                    result.append(sublist)
            if i + j > n:
                sublist = circular_list[i:] + circular_list[:(i + j) % n]
                if product(sublist) == -61:
                    result.append(sublist)
    return result