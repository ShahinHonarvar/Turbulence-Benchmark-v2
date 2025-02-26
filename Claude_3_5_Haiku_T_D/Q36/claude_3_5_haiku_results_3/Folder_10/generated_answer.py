def filter_chars(s):
    chars_to_remove = set()
    for i in range(36, 60):
        if '!' < s[i] < 'B':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result