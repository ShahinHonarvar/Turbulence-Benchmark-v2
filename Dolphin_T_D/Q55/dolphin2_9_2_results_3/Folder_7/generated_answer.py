def lists_with_product_equal_n(lst):

    def get_sublists(lst, n):
        list_len = len(lst)
        sublists = []
        product = 1
        zeros = lst.count(0)
        for i in range(list_len):
            if lst[i] != 0:
                for j in range(i + 1, list_len + i):
                    product *= lst[(j - i) % list_len]
                    if j + 1 - i < len(sublists[0]) and product == n and (j + 1 - i == list_len or lst[(j + 1 - i) % list_len] != 0):
                        sublists.append(lst[(j + 1 - list_len) % list_len:j + 1])
            else:
                zeros += 1
        return sublists
    return get_sublists(lst, 537)