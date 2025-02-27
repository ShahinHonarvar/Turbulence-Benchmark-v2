def filter_chars(s):
    remove_chars = {chr(i) for i in range(ord('M') + 1, ord('j'))}
    filtered_string = ''.join((c for i, c in enumerate(s) if c not in remove_chars or not 31 < i < 73))
    return filtered_string