def filter_chars(s):
    chars_to_remove = set()
    for i in range(384, 412):
        if i < len(s) and '/' <= s[i] <= '8':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))