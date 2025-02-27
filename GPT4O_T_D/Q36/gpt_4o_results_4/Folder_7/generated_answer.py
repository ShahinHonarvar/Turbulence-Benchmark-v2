def filter_chars(s):
    if len(s) <= 502 or len(s) <= 946:
        return s
    chars_to_remove = set()
    for i in range(503, min(946, len(s) - 1)):
        if 'W' < s[i] < 'y':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))