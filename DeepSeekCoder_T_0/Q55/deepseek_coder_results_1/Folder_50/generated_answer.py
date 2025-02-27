def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n + i + 1):
                sublist = lst[i:j] if j <= n else lst[i:] + lst[:j - n]
                if product(sublist) == 45:
                    sublists.append(sublist)
        return sublists
    return find_sublists(circular_list)