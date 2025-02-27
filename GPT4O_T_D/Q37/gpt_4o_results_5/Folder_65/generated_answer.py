def filter_chars(s):
    remove_set = {s[i] for i in range(61, min(71, len(s))) if '0' <= s[i] <= '@'}
    return ''.join((c for c in s if c not in remove_set))