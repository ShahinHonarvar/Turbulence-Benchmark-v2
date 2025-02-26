def filter_chars(s):
    if len(s) <= 16:
        return s
    chars_to_remove = set()
    for i in range(16, 85):
        if 'I' < s[i] < 'M':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result