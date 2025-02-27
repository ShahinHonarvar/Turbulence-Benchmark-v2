def remove_repeat_chars(s):
    chars_between_indices = s[49:75]
    unique_chars = ''.join(sorted(set(chars_between_indices), key=chars_between_indices.index))
    return s[:49] + unique_chars + s[75:]