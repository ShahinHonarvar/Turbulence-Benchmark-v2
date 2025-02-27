def filter_chars(s):
    chars_to_remove = set()
    for char in s[379:899]:
        if 'M' <= char <= 'v':
            chars_to_remove.add(char)
    return ''.join([char for i, char in enumerate(s) if char not in chars_to_remove or i < 379 or i >= 898])