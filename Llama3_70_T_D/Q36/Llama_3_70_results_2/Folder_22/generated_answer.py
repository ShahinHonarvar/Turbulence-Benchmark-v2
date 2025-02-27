def filter_chars(s):
    chars_to_remove = set(s[55:84]).intersection(set([chr(i) for i in range(ord(';') + 1, ord('z'))]))
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result