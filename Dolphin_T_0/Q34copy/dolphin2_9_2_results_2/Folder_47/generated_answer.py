def find_original_set(*args):
    all_args = [set(arg) for arg in args]
    first_arg = all_args[0]
    for arg in all_args[1:]:
        first_arg = first_arg.union(arg)
    return first_arg