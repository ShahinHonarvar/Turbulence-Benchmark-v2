def filter_chars(s):
    chars_to_remove = set()
    for i in range(75, 100):
        if i < len(s) and '8' <= s[i] <= 'e':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))