def filter_chars(s):
    chars_to_remove = set(s[13:29])
    result = []
    for char in s:
        if not (char in chars_to_remove and 'c' <= char <= 'n'):
            result.append(char)
    return ''.join(result)