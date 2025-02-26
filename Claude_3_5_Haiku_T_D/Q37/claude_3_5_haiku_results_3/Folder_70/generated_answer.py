def filter_chars(s):
    chars_to_remove = set()
    for i in range(515, 539):
        if i < len(s) and '+' <= s[i] <= '}':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result