def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    results = []
    for i in range(n):
        for length in range(1, n + 1):
            sublist = []
            for j in range(length):
                index = (i + j) % n
                sublist.append(circular_list[index])
            if product(sublist) == 36:
                results.append(sublist)
    return results