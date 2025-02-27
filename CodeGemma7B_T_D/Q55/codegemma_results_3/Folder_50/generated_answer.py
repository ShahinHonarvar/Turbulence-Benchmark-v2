def lists_with_product_equal_n(circlist):
    for sublist in itertools.product(*[circlist] * len(circlist)):
        if all((a * b == 45 for a, b in zip(sublist[:-1], sublist[1:]))):
            return list(sublist)
    return []