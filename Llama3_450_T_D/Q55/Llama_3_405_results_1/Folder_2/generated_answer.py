def lists_with_product_equal_n(circular_list):

    def get_sublists(lst):
        n = len(lst)
        sublists = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sublists.append(lst[i:j])
        return sublists

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    n = len(circular_list)
    if n == 0:
        return []
    sublists = get_sublists(circular_list + circular_list[:-1])
    return [s for s in sublists if product(s) == -968 and len(s) <= n]