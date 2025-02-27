def filter_chars(s):
    chars_to_remove = set()
    for i in range(35, 52):
        if len(s) > i and 'H' <= s[i] <= 's':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s