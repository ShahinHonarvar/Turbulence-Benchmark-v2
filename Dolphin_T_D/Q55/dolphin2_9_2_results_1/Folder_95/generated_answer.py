def lists_with_product_equal_n(lst):

    def get_sublists(lst, product, start, end):
        if start == end and product == 1:
            result.append(lst[:])
            return
        if start == end:
            return
        for i in range(start, end + 1):
            get_sublists(lst, product / lst[i], start, i - 1)
            get_sublists(lst, product / lst[i], i + 1, end)
            lst.pop(i)
            get_sublists(lst, product / lst[i], start, i - 1)
            get_sublists(lst, product / lst[i], i + 1, end)
            lst.insert(i, lst[i])
    result = []
    get_sublists(lst, 28, 0, len(lst) - 1)
    return result