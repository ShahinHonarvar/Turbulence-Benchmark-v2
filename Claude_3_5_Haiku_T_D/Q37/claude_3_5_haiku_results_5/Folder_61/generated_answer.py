def filter_chars(s):
    chars_to_remove = set()
    for i in range(5, 7):
        if 0 <= i < len(s) and 'G' <= s[i] <= 'p':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))