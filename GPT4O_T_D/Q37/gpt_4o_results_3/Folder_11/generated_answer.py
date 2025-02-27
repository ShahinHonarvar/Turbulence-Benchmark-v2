def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 97:
        for i in range(29, 98):
            if '-' <= s[i] <= 'n':
                chars_to_remove.add(s[i])
    else:
        for i in range(29, len(s)):
            if '-' <= s[i] <= 'n':
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))