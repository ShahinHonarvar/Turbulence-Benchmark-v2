def filter_chars(s):
    chars_to_remove = set()
    for i in range(38, 100):
        if 65 <= ord(s[i]) <= 81:
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])