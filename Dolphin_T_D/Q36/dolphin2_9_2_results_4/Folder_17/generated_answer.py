def filter_chars(s):
    chars = [s[i] for i in range(18, 95) if 'K' < s[i] < 'a']
    for char in chars:
        s = s.replace(char, '')
    return s