def composite_nums_between_indices(ls):
    return {i for i in set(ls[62:79]) if i > 1 and (not all((i % j for j in range(2, i))))} if len(ls) > 78 else set()