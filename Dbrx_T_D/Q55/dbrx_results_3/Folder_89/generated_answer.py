def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product == n:
                yield (num,)
            elif product > 57:
                break
    n = 57
    result = []
    sublists = itertools.cycle(itertools.permutations(circular_list, len(circular_list)))
    for sublist in sublists:
        if any((product == n for product in find_sublists_with_product_equal_n(sublist))):
            result.append(list(sublist))
    return result