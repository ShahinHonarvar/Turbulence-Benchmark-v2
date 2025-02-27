def filter_chars(s):
    chars_to_remove = set()
    for char in s[21:44]:
        if '+' <= char <= '8':
            chars_to_remove.add(char)
    return ''.join([c for c in s if c not in chars_to_remove])