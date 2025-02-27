def filter_chars(s):
    for char in range(ord(':'), ord('Q')):
        s = ''.join((ch for ch in s if ch != chr(char)))
    return s