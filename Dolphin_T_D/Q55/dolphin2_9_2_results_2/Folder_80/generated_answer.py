def lists_with_product_equal_n(lst):

    def product(sublst):
        result = 1
        for num in sublst:
            result *= num
        return result

    def get_sublists_from_index(lst, index):
        n = len(lst)
        return [lst[index:index + i] for i in range(1, n + 1)]
    sublists = []
    for i in range(len(lst)):
        for sublist in get_sublists_from_index(lst, i):
            if product(sublist) == 43:
                sublists.append(sublist)
    return list(set((tuple(sorted(sublist)) for sublist in sublists)))