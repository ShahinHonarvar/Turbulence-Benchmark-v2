def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        n = len(lst)
        for start in range(n):
            for end in range(start + 1, n + 1):
                sublist = lst[start:end]
                if product(sublist) == 13:
                    sublists.append(sublist)
        return sublists
    n = len(circular_list)
    circular_list += circular_list
    all_sublists = find_sublists(circular_list)
    result = []
    for sublist in all_sublists:
        if sublist not in result and len(sublist) <= n:
            result.append(sublist)
    return result