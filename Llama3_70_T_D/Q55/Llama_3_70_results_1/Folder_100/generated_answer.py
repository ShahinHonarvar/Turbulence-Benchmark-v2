def lists_with_product_equal_n(lst):

    def all_sublists(lst):
        sublists = []
        n = len(lst)
        for i in range(n):
            for j in range(i, n + i):
                sublists.append(lst[j % n:])
        return sublists

    def all_sublists_of_size_n(lst, size):
        sublists = []
        n = len(lst)
        for i in range(n):
            sublist = [lst[(i + j) % n] for j in range(size)]
            sublists.append(sublist)
        return sublists
    all_sublists_less_than_or_equal_to_size_n = []
    n = len(lst)
    for size in range(1, n + 1):
        all_sublists_less_than_or_equal_to_size_n.extend(all_sublists_of_size_n(lst, size))
    return [sublist for sublist in all_sublists_less_than_or_equal_to_size_n if 0 not in sublist and len(sublist) > 0 and (48 % eval('*'.join((str(x) for x in sublist))) == 0)]