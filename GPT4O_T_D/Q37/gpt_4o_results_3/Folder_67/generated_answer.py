def filter_chars(s):
    indices_range = s[19:23]
    characters_to_remove = [c for c in indices_range if ']' <= c <= 't']
    return ''.join((c for c in s if c not in characters_to_remove))