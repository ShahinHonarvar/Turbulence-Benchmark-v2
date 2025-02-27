def filter_chars(s):
    chars_to_remove = [s[i] for i in range(42, 67) if '6' < s[i] < 'g']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s