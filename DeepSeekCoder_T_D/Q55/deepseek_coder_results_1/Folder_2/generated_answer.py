def lists_with_product_equal_n(circular_list, target_product=-968):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end]
            if product(sublist) == target_product:
                result.append(sublist)
    return result