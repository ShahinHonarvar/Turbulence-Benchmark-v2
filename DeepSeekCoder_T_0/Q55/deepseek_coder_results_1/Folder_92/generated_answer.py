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
                sublist = lst[i:j]
                if product(sublist) == 5:
                    sublists.append(sublist)
        return sublists
    result = find_sublists(circular_list)
    extended_list = circular_list + circular_list
    extended_result = find_sublists(extended_list)
    for sublist in extended_result:
        if len(sublist) > len(circular_list):
            break
        if sublist not in result:
            result.append(sublist)
    return result