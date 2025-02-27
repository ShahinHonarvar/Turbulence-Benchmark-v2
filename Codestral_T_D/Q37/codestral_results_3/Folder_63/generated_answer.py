def filter_chars(s):
    for c in range(ord('/'), ord('a') + 1):
        s = ''.join((char for char in s if not (42 <= s.index(char) <= 92 and ord(char) == c)))
    return s