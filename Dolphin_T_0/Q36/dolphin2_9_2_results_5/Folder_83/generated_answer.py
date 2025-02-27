def filter_chars(s):
    chars_to_remove = [s[i] for i in range(72, 93) if '<' < s[i] < 'J']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s