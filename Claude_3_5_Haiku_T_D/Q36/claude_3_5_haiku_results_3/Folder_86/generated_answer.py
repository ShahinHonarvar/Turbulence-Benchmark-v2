def filter_chars(s):
    chars_to_remove = set()
    for i in range(673, 709):
        if 'X' < s[i] < '}':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result