def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 27:
        for i in range(27, min(len(s), 30)):
            if ';' <= s[i] <= 'b':
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))