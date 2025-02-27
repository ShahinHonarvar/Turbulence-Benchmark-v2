def filter_chars(s):
    chars_to_remove = set()
    for i in range(max(0, 75), min(len(s), 100)):
        if '8' <= s[i] <= 'e':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))