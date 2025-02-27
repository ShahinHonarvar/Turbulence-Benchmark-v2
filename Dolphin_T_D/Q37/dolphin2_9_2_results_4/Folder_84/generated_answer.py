def filter_chars(s):
    chars_to_remove = [s[i] for i in range(138, 921) if 6 <= s[i] <= 'A']
    for char in chars_to_remove:
        s = ''.join([x for x in s if x != char])
    return s