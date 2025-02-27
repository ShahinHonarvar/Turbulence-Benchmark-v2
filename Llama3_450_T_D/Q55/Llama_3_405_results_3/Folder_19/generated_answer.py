def lists_with_product_equal_n(lst):

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
            for j in range(i):
                sublists.append(lst[i:] + lst[:j])
        return sublists
    return [sublist for sublist in get_sublists(lst) if product(sublist) == -54]