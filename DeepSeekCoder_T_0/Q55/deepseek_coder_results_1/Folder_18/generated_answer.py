def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sub = lst[i:j]
                if product(sub) == 36:
                    sublists.append(sub)
        return sublists
    all_sublists = find_sublists(circular_list)
    circular_sublists = find_sublists(circular_list + circular_list)
    for sub in circular_sublists:
        if sub not in all_sublists and len(sub) <= len(circular_list):
            all_sublists.append(sub)
    return all_sublists