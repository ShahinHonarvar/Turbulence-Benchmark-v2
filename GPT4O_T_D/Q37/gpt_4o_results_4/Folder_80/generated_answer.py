def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 79:
        for char in s[36:80]:
            if 'a' <= char <= 'i':
                chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result