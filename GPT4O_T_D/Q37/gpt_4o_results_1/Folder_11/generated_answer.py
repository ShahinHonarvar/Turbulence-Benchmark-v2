def filter_chars(s):
    if len(s) <= 29:
        return s
    filtered_chars = set(s[29:98])
    target_chars = {chr(i) for i in range(ord('-'), ord('n') + 1)}
    removal_chars = filtered_chars.intersection(target_chars)
    return ''.join((c for c in s if c not in removal_chars))