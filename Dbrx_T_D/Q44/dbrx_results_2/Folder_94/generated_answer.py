def composite_nums_between_indices(arg):
    if len(arg) < 55 or 27 > len(arg):
        return set()
    return {i for i in arg[27:56] if i > 1 and (not all((i % j for j in range(2, i))))}