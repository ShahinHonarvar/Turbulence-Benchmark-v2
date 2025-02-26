def filter_chars(s):
    chars_to_remove = [s[i] for i in range(58, 69) if '(' < s[i] < 'W']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s