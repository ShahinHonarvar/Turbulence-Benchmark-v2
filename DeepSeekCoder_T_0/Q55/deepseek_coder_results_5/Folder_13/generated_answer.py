def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst, n):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublist = lst[i:j]
                if product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    n = 54
    all_sublists = find_sublists(circular_list, n)
    circular_sublists = find_sublists(circular_list + circular_list[:-1], n)
    unique_circular_sublists = []
    seen = set()
    for sublist in circular_sublists:
        if tuple(sublist) not in seen:
            unique_circular_sublists.append(sublist)
            seen.add(tuple(sublist))
    return unique_circular_sublists if unique_circular_sublists else all_sublists