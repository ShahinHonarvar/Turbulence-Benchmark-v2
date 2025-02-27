def filter_chars(s):
    chars_to_remove = [s[i] for i in range(78, 81) if 'S' < s[i] < '[']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s