def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        i = 0
        while i < len(lst):
            cur = lst[i]
            for j in range(i + 1, len(lst) + 1):
                cur *= lst[j % len(lst)]
                if cur == n:
                    sublists.append(lst[i:j])
            i += 1
        return sublists
    n = 49
    sublists = get_sublists(lst)
    result = [i for i in sublists if all((i not in j for j in sublists if i != j))]
    return result