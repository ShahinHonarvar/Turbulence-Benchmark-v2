def filter_chars(s):
    chars_to_remove = [s[i] for i in range(343, 665) if s[i] > '%' and s[i] < 'U']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s