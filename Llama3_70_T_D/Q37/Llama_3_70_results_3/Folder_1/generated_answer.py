def filter_chars(s):
    chars_to_remove = set()
    for i in range(41, 80):
        if i < len(s) and 'f' <= s[i] <= '|':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))