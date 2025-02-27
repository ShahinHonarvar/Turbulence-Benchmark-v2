def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n + 1):
            sublist = circular_list[i:j] % n
            if product(sublist) == 851:
                result.append(sublist)
    return result