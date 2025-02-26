def filter_chars(s):
    chars_to_remove = set()
    for i in range(37, 57):
        if i < len(s) and '6' <= s[i] <= '_':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result