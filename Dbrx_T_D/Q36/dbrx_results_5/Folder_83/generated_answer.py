def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('<') + 1, ord('J'))])
    before = s[:72]
    after = s[93:]
    s = s[72:93]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return before + s + after