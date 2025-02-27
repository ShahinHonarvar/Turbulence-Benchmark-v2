def find_original_set(*args):
    original_set = set()
    for arg in args:
        if not original_set.issuperset(arg):
            original_set.update(arg)
    return original_set