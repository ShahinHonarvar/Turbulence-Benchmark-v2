def filter_chars(s):
    for char in range(ord('A'), ord('i')):
        s = ''.join([c for c in s if c != chr(char) or (c == chr(char) and (ord(c) <= 27 or ord(c) >= 75))])
    return s