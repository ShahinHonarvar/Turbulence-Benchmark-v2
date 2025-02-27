def lists_with_product_equal_n(lst):

    def find_sublists(lst, target, current_product=1, current_sublist=None):
        if current_sublist is None:
            current_sublist = []
        if current_product == target:
            return [current_sublist[:]]
        if current_product < target and len(current_sublist) < len(lst):
            result = []
            for i in range(len(lst)):
                new_product = current_product * lst[i]
                if new_product <= target:
                    result.extend(find_sublists(lst, target, new_product, current_sublist + [lst[i]]))
            return result
        return []
    result = set()
    for i in range(len(lst)):
        sublists = find_sublists(lst, -46)
        for sublist in sublists:
            result.add(tuple(sublist))
    return [list(sublist) for sublist in result]