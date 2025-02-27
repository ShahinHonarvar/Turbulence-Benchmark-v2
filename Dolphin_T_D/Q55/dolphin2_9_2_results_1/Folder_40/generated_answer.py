def lists_with_product_equal_n(lst):

    def get_combination_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(lst)
    sublists = set()
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size]
            if get_combination_product(sublist) == -9:
                sublists.add(tuple(sublist))
    return [list(sublist) for sublist in sublists]