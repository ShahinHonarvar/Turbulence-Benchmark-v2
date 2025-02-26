def filter_chars(s):
    if len(s) <= 2:
        return s
    chars_to_remove = set()
    for i in range(2, len(s) - 1):
        if '3' < s[i] < '^':
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result