def filter_chars(s):
    chars = {}
    for i, char in enumerate(s):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            chars[char] = chars.get(char, 0) + 1
    for char in chars:
        s = s.replace(char, '')
    return s