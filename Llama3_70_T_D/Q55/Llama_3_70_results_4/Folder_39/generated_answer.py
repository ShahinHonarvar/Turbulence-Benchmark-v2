def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            sublist = []
            for j in range(len(lst)):
                sublist.append(lst[(i + j) % len(lst)])
                sublists.append(sublist[:])
        return sublists
    result = []
    for sublist in get_sublists(lst):
        if len(sublist) > 0 and len(sublist) <= len(lst):
            if eval('*'.join(map(str, sublist))) == -46:
                result.append(sublist)
    return result