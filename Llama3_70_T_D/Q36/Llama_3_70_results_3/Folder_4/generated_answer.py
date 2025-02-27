def filter_chars(s):

    def is_valid_char(c):
        return not '6' < c < 'g'
    valid_chars = [c for c in s[:42]] + [c for c in s[42:67] if is_valid_char(c)] + [c for c in s[67:]]
    for char in set(s[42:67]):
        if '6' < char < 'g':
            valid_chars = [c for c in valid_chars if c != char]
    return ''.join(valid_chars)