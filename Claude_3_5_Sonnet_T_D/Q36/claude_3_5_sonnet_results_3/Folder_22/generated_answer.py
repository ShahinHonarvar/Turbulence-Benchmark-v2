def filter_chars(s):
    characters_to_remove = set()
    for i in range(56, 84):
        if i < len(s) and ';' < s[i] < 'z':
            characters_to_remove.add(s[i])
    return ''.join((char for char in s if char not in characters_to_remove))