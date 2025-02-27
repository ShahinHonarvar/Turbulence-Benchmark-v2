def lists_with_product_equal_n(circular_list, n=90):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublist = lst[i:j]
                if product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    all_sublists = find_sublists(circular_list)
    circular_list_extended = circular_list + circular_list
    all_sublists.extend(find_sublists(circular_list_extended))
    unique_sublists = []
    seen = set()
    for sublist in all_sublists:
        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            unique_sublists.append(sublist)
    return unique_sublists