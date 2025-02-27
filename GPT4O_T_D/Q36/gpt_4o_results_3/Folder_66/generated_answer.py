def filter_chars(s):
    remove_set = set(s[40:87])
    return ''.join((c for c in s if c not in remove_set or c <= '!' or c >= '}'))