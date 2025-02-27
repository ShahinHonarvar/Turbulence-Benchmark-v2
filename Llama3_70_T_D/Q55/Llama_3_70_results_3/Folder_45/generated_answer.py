def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        sublists = [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]
        return sublists + [lst[i:] + lst[:j] for i in range(len(lst)) for j in range(i)]
    sublists = circular_sublists(lst)
    result = [sublist for sublist in sublists if len(sublist) <= len(lst) and eval('*'.join(map(str, sublist))) == -5]
    return result