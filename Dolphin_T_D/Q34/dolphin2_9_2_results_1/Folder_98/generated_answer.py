def find_original_set(*args):
    if len(args) != 9:
        return 'Error: Invalid number of arguments.'
    union_set = set()
    for i in args:
        if type(i) != set:
            return 'Error: Input should be a set of integers.'
        union_set = union_set.union(i)
    return union_set