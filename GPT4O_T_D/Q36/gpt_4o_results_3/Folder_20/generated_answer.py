def filter_chars(s):
    characters_to_remove = set()
    for i in range(14, 40):
        if s[i] > ':' and s[i] < 'C':
            characters_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in characters_to_remove))