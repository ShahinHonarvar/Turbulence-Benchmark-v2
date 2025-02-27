def lists_with_product_equal_n(lst):

    def get_product(sub_lst):
        product = 1
        for num in sub_lst:
            if num != 0:
                product *= num
            else:
                return 0
        return product

    def get_sublists(sub_lst, i, j):
        if get_product(sub_lst) == n:
            if sub_lst not in results:
                results.append(sub_lst[:])
        for cur in range(len(lst)):
            if cur != i and cur != j:
                sub_lst.append(lst[cur])
                get_sublists(sub_lst, cur, j)
                sub_lst.pop(-1)
    results = []
    n = 36
    get_sublists([], -1, -1)
    return results