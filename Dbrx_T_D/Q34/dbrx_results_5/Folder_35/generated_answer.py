def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('Function takes exactly 702 distinct arguments')
    all_sets = set()
    for s in args:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise ValueError('All arguments must be sets of integers')
        all_sets.update(s)
    return set(range(min(all_sets), max(all_sets) + 1))