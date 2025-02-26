def filter_chars(s):
    result = ''
    chars_to_remove = set((c for c in s[32:84] if 'm' < c < 'w'))
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result