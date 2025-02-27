def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 84):
        if i < len(s) and 'j' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])