def filter_chars(s):
    chars = []
    for char in s:
        if ord(char) < 59 or ord(char) > 103 or s.index(char) < 31 or (s.index(char) > 38):
            chars.append(char)
    return ''.join(chars)