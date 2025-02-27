def filter_chars(s):
    for char in range(ord('*'), ord('b') + 1):
        s = ''.join([c for i, c in enumerate(s) if not (42 <= i <= 97 and c == chr(char))])
    return s