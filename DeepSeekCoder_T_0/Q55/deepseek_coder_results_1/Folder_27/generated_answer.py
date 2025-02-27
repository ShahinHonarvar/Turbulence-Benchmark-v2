def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        n = len(lst)
        for start in range(n):
            for end in range(start + 1, start + n + 1):
                sublist = lst[start:end]
                if product(sublist) == -82:
                    sublists.append(sublist)
        return sublists
    circular_list += circular_list
    return find_sublists(circular_list)