def filter_chars(s):
    chars_to_remove = [s[i] for i in range(669, 888) if s[i] > 'B' and s[i] < 'Y']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s