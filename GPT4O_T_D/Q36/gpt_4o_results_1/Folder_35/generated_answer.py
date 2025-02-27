def filter_chars(s):
    characters_to_remove = set((chr(i) for i in range(ord('(') + 1, ord(']'))))
    modified_string = s[:163] + ''.join((c for c in s[163:658] if c not in characters_to_remove)) + s[658:]
    return modified_string