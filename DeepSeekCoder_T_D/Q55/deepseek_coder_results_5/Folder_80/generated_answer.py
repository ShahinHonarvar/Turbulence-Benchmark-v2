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
                if product(sublist) == 43:
                    sublists.append(sublist)
        return sublists
    if not circular_list:
        return []
    circular_list *= 2
    result = find_sublists(circular_list)
    return result