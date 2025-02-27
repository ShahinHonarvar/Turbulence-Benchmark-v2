def find_original_set(*args):
    if len(args) != 194:
        return f'Function requires exactly 194 arguments. {len(args)} were given'
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set