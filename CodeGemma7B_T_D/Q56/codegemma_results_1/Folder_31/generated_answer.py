def all_substring_of_size_n(txt):
    if len(txt) >= 46:
        return set((''.join(x) for x in itertools.combinations(txt, 46)))
    return []