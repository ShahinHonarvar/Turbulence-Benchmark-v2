def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        return sublists

    def get_circular_sublists(lst):
        sublists = get_sublists(lst)
        for i in range(len(lst)):
            sublists.append(lst[i:] + lst[:i])
        return sublists
    all_sublists = get_circular_sublists(circular_list)
    return [sublist for sublist in all_sublists if product(sublist) == -30]