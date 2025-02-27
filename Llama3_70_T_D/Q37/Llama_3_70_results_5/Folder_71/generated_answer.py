def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(32, 47) if '0' <= chr(i) <= 'k'])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result