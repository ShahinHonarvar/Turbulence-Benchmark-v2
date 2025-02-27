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
    circular_list += circular_list
    all_sublists = find_sublists(circular_list)
    result = []
    for sublist in all_sublists:
        if sublist not in result and len(sublist) <= len(circular_list) // 2:
            result.append(sublist)
    return result