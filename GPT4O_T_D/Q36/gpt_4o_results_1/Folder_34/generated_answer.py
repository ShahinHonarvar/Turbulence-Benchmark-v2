def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('?') + 1, ord('m'))))
    remove_indices = range(10, 79)
    characters_to_remove = {s[i] for i in remove_indices if i < len(s) and s[i] in chars_to_remove}
    return ''.join((c for c in s if c not in characters_to_remove))