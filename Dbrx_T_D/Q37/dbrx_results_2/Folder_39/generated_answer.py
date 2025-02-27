def filter_chars(s):
    chars_to_remove = [chr(x) for x in range(ord('A'), ord('V'))]
    char_set = set(chars_to_remove[20:52])
    filtered_chars = [c for c in s if c not in char_set]
    return ''.join(filtered_chars)