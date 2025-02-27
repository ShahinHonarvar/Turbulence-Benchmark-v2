def find_original_set(*args):
    min_set = min(args, key=len)
    for subset in min_set:
        if not all((subset in other_set for other_set in args if other_set != min_set)):
            min_set.remove(subset)
    return min_set