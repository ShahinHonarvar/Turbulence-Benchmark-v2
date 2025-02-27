def filter_chars(s):
    if len(s) < 125:
        return s
    chars_to_remove = set()
    for i in range(124, min(855, len(s))):
        if '9' <= s[i] <= 's':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))