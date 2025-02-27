def filter_chars(s):
    if len(s) <= 636:
        return s
    filtered_string = s[:171]
    chars_to_remove = set((c for c in s[172:636] if 'c' < c < 's'))
    for char in s[171:]:
        if char not in chars_to_remove:
            filtered_string += char
    return filtered_string