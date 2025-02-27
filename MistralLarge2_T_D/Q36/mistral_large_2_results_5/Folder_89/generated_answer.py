def filter_chars(s):
    characters_to_remove = {s[i] for i in range(57, 69) if '(' < s[i] < 'W'}
    return ''.join((c for c in s if c not in characters_to_remove))