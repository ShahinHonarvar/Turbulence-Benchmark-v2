def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, min(84, len(s))):
        if 'j' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))