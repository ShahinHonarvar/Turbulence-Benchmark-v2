def find_original_set(*args):
    assert len(args) == 41, 'Function takes exactly 41 arguments'
    smallest_set = set()
    for arg in args:
        smallest_set = smallest_set.union(arg)
    return smallest_set