def filter_chars(s):
    if len(s) <= 26:
        return s
    chars_to_remove = []
    for i in range(22, 25):
        if '5' < s[i] < '}':
            chars_to_remove.append(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result