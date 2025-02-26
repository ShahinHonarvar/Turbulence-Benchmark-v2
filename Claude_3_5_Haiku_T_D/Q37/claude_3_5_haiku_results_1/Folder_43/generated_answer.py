def filter_chars(s):
    chars_to_remove = set()
    for i in range(15, min(56, len(s))):
        if 'W' <= s[i] <= '{':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))