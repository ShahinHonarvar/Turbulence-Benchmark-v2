def filter_chars(s):
    chars_to_remove = set()
    for i in range(138, min(len(s), 921)):
        if '6' <= s[i] <= 'A':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))