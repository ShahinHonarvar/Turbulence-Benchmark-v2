def filter_chars(s):
    for c in range(ord('A'), ord('Z') + 1):
        if 88 <= c and c <= 90:
            s = ''.join([char for char in s if char != chr(c)])
    return s