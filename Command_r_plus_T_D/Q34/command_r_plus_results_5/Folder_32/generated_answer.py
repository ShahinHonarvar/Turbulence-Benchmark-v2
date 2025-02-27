def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Exactly 459 arguments are required.')
    if not all((isinstance(s, set) and s.issubset(set(range(1, 460))) for s in args)):
        raise ValueError('All arguments must be distinct sets of integers from 1 to 459.')
    original_set = set.union(*args)
    min_set = set()
    for num in range(1, 460):
        if all((num in s for s in args)):
            min_set.add(num)
    return min_set