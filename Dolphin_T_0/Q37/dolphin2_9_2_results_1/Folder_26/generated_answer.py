def filter_chars(s):
    ref_chars = s[20:63]
    for char in ref_chars:
        if char >= 'i' and char <= 'k':
            s = s.replace(char, '')
    return s