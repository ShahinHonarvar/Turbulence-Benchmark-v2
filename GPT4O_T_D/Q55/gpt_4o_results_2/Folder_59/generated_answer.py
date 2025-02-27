def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                idx = (start + i) % n
                sublist.append(circular_list[idx])
            if product(sublist) == -3:
                result.append(sublist)
    return result