def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for number in sublist:
            result *= number
        return result
    sublists = []
    for size in range(len(lst) + 1):
        for i in range(len(lst)):
            if size == 0 or product(lst[i:i + size]) == -18:
                sublists.append(lst[i:i + size])
    return list(set((tuple(sublist) for sublist in sublists)))