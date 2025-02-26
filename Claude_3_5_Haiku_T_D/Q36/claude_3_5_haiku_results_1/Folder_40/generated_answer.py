def filter_chars(s):
    if len(s) <= 2:
        return s
    chars_to_remove = set()
    for i in range(2, 7):
        if ord('-') < ord(s[i]) < ord('L'):
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result