def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(lst)
    lst = lst * 2
    sublists = []
    for start in range(n):
        for size in range(1, n + 1):
            current_list = lst[start:start + size]
            if product(current_list) == -44:
                sublists.append(current_list)
    return sublists