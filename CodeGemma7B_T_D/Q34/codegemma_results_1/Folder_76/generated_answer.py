def find_original_set(*args):
    max_length = max((len(s) for s in args))
    original_set = set()
    for i in range(max_length + 1):
        for s in args:
            if len(s) == i:
                if s.issubset(original_set):
                    original_set.difference_update(s)
                else:
                    original_set.update(s)
    return original_set