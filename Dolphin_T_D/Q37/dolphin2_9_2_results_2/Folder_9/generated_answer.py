def filter_chars(s):
    chars = set()
    for i in range(38, 100):
        if 'A' <= s[i] <= 'Q':
            chars.add(s[i])
    return s.translate(str.maketrans('', '', ''.join(chars)))