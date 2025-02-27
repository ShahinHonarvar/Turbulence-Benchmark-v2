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
                if product(sub) == 51:
                    sublists.append(sub)
        return sublists
    result = find_sublists(circular_list)
    extended_list = circular_list + circular_list
    extended_result = find_sublists(extended_list)
    for sub in extended_result:
        if len(sub) <= len(circular_list) and sub not in result:
            result.append(sub)
    return result