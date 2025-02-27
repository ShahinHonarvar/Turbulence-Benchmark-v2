def filter_chars(s):
    for c in range(ord('5'), ord('f')):
        s = ''.join([ch for ch in s if ch != chr(c)])
    return s