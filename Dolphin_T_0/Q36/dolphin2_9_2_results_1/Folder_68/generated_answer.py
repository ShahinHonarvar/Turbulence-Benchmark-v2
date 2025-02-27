def filter_chars(s):
    chars_to_filter = [s[i] for i in range(1, 9) if '8' < s[i] < 'm']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s