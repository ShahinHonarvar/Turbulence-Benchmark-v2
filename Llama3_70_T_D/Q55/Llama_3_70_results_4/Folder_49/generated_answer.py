def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def circular_sublists(lst):
        sublists = get_sublists(lst)
        for i in range(len(lst)):
            sublists.append(lst[i:] + lst[:i])
        return sublists
    result = []
    for i in range(len(lst)):
        for sublist in circular_sublists(lst[i:] + lst[:i]):
            if len(sublist) <= len(lst) and 0 not in sublist and (eval('*'.join(map(str, sublist))) == -61):
                result.append(sublist)
    return result