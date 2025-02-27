def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def generate_sublists(clist, start, end):
        n = len(clist)
        sublists = []
        while start != end:
            sublist = []
            j = start
            while j != end:
                sublist.append(clist[j])
                sublists.append(sublist.copy())
                j = (j + 1) % n
            start = (start + 1) % n
        return sublists
    n = len(circular_list)
    all_sublists = generate_sublists(circular_list, 0, 0)
    result = []
    for sublist in all_sublists:
        if product(sublist) == -87:
            result.append(sublist)
    return result