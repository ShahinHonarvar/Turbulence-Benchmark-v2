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
                if product(sub) == 49:
                    sublists.append(sub)
        return sublists
    result = find_sublists(circular_list)
    circular_result = find_sublists(circular_list + circular_list[:-1])
    for sub in circular_result:
        if sub not in result and len(sub) <= len(circular_list):
            result.append(sub)
    return result