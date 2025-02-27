def lists_with_product_equal_n(circular_list):

    def is_sublist(sub, main):
        sub_len = len(sub)
        main_len = len(main)
        if sub_len > main_len:
            return False
        if sub_len == main_len:
            return sub == main
        for i in range(main_len - sub_len + 1):
            if sub == main[i:i + sub_len]:
                return True
        return False

    def prod(lst):
        p = 1
        for a in lst:
            p *= a
        return p
    n = len(circular_list)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            if prod(circular_list[i:j]) == -1 and (not is_sublist(circular_list[i:j], circular_list[j % n:i] + circular_list[j % n:]) in sublists):
                sublists.append(circular_list[i:j])
    return sublists