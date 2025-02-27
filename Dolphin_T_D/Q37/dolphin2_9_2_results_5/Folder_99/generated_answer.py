def filter_chars(s):
    chars_to_remove = []
    for i in range(373, 902):
        if s[i] >= 'T' and s[i] <= 'h':
            chars_to_remove.append(s[i])
    modified_s = ''
    for char in s:
        if char not in chars_to_remove:
            modified_s += char
    return modified_s