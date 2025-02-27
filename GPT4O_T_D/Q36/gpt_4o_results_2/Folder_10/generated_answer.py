def filter_chars(s):
    filtered = s[35:60]
    chars_to_remove = {chr(i) for i in range(ord('!'), ord('B'))}
    for char in filtered:
        if char in chars_to_remove:
            s = s.replace(char, '')
    return s