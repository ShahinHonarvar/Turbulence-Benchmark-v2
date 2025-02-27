def filter_chars(s):
    chars = [chr(i) for i in range(28, 66) if 'O' <= chr(i) <= 'd']
    for char in chars:
        s = s.replace(char, '')
    return s