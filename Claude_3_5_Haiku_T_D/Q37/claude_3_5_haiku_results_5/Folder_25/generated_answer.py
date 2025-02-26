def filter_chars(s):
    chars_to_remove = set()
    for i in range(31, 39):
        if i < len(s) and ';' <= s[i] <= 'g':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))