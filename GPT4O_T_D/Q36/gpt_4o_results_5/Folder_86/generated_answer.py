def filter_chars(s):
    target_indices = range(673, 709)
    filter_set = {chr(i) for i in range(ord('X') + 1, ord('}'))}
    chars_to_remove = {s[i] for i in target_indices if i < len(s) and s[i] in filter_set}
    return ''.join((c for c in s if c not in chars_to_remove))