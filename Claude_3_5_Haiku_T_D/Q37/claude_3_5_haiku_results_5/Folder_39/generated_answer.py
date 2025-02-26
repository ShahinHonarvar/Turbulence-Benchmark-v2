def filter_chars(s):
    chars_to_remove = set()
    for i in range(52, 82):
        if i < len(s) and 'A' <= s[i] <= 'U':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))