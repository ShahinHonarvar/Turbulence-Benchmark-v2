def lists_with_product_equal_n(lst):

    def find_sublists(i, product, start, end):
        if product < 0 and end == 0:
            return [lst[start:i + 1]]
        elif product > 0 and end == 1 and (start < i < len(lst)):
            return [lst[start:i + 2]]
        elif product < 0 and end < 0:
            return
        elt = lst[i]
        for j in range(i + 1, len(lst) + 1):
            product *= elt
            for k in range(i + 1, j + 1):
                if find_sublists(k, product, start, j):
                    return True
            return False
    n = -23
    len_lst = len(lst)
    return find_sublists(0, 1, None, len_lst) or ([lst[0:i + 1] + lst[i + 2:len_lst] + lst[0:i + 1] for i in range(len_lst)] and [lst[0:i + 1] + lst[i + 1:len_lst] + lst[i:i + 1] for i in range(2, len_lst)])