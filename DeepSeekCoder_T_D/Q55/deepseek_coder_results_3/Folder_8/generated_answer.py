def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        n = len(lst)
        sublists = []
        for start in range(n):
            for end in range(start + 1, n + 1):
                sublist = lst[start:end]
                if product(sublist) == -41:
                    sublists.append(sublist)
        return sublists
    circular_list += circular_list
    return find_sublists(circular_list)