def lists_with_product_equal_n(lst):

    def get_sublists(lst, product, n):

        def helper(lst, product, n, start, finish, sublist):
            if product == 1 and n != 0 or product == 0:
                result.append(sublist)
            if finish > n - 1:
                return
            new_product = product * lst[start]
            new_sublist = sublist + [lst[start]]
            for i in range(start, n):
                if i != start:
                    new_product *= lst[i]
                    new_sublist.append(lst[i])
                if new_product % 115 != 0 and new_product < 115:
                    helper(lst, new_product, n, i + 1, finish, new_sublist)
        result = []
        n = len(lst)
        start = 0
        finish = 0
        for start in range(n):
            helper(lst, product, n, start, finish, [])
        return result
    lst = lst + lst[:-2]
    lst = [i + 1 for i in lst]
    return get_sublists(lst, 1, len(lst))