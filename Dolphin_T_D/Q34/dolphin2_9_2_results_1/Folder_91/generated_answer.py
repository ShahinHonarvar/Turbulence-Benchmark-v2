def find_original_set(arg1, arg2, arg3, arg4, arg5):
    if not (isinstance(arg1, set) and isinstance(arg2, set) and isinstance(arg3, set) and isinstance(arg4, set) and isinstance(arg5, set)):
        return 'Error: All arguments must be sets of integers'
    return set.union(arg1, arg2, arg3, arg4, arg5)