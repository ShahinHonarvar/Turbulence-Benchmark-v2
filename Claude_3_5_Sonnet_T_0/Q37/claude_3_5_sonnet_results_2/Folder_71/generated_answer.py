def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for i in range(32, 47):
        if i < len(s) and '0' <= s[i] <= 'k':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result