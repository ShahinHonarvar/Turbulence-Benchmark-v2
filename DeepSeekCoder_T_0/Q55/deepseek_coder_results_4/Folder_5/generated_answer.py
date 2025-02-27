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
            for end in range(start + 1, n + 1):
                sublist = lst[start:end]
                if product(sublist) == -33:
                    sublists.append(sublist)
        return sublists
    n = len(circular_list)
    circular_list += circular_list
    all_sublists = find_sublists(circular_list)
    result = []
    for sublist in all_sublists:
        if len(sublist) <= n:
            result.append(sublist)
    return result