def lists_with_product_equal_n(lst):

    def contiguous_sublists(lst):
        result = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == 13:
                    result.append(lst[i:j + 1])
                elif product > 13:
                    break
        return result
    result = []
    for i in range(len(lst)):
        sublists = contiguous_sublists(lst[i:] + lst[:i])
        result.extend(sublists)
    result = set((tuple(sorted(sublist)) for sublist in result))
    return [list(sorted(sublist)) for sublist in result]