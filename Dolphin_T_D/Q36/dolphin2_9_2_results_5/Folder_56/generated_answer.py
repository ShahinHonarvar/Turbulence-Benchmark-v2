def filter_chars(s):
    chars = [c for c in s]
    for i in range(31, 50):
        if '/' < chars[i] < 'J':
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)