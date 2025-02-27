def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_all_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def get_circular_sublists(lst):
        circular_sublists = get_all_sublists(lst)
        for i in range(len(lst)):
            circular_sublists.append(lst[i:] + lst[:i])
        return circular_sublists
    circular_sublists = get_circular_sublists(lst)
    return [sublist for sublist in circular_sublists if product(sublist) == -91]