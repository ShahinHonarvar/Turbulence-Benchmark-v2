def filter_chars(s):
    if len(s) < 43:
        return s
    remove_chars = set()
    end_index = min(len(s) - 1, 97)
    for c in s[42:end_index + 1]:
        if '*' <= c <= 'b':
            remove_chars.add(c)
    return ''.join((c for c in s if c not in remove_chars))