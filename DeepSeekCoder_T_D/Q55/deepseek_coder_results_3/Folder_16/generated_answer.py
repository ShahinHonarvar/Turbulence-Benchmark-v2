def lists_with_product_equal_n(circular_list, n=-837):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            for end in range(start + 1, len(lst) + 1):
                sublist = lst[start:end]
                if product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    circular_list += circular_list
    return find_sublists(circular_list)