def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        n = len(lst)
        sublists = []
        for start in range(n):
            for end in range(start + 1, n + 1):
                sublist = lst[start:end]
                if product(sublist) == 733:
                    sublists.append(sublist)
        return sublists
    result = find_sublists(circular_list)
    circular_result = find_sublists(circular_list + circular_list[:-1])
    for sublist in circular_result:
        if sublist not in result and len(sublist) <= len(circular_list):
            result.append(sublist)
    return result