def filter_chars(s):
    excluded_indices = range(220, 403)
    chars_to_remove = {chr(i) for i in range(ord('*') + 1, ord('7'))}
    chars_at_indices = {s[i] for i in excluded_indices if s[i] in chars_to_remove}
    return ''.join((c for c in s if c not in chars_at_indices))