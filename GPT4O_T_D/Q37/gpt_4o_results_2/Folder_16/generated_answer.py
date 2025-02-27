def filter_chars(s):
    characters_to_remove = set()
    for i in range(225, 382):
        if 'D' <= s[i] <= 'Y':
            characters_to_remove.add(s[i])
    return ''.join((c for c in s if c not in characters_to_remove))