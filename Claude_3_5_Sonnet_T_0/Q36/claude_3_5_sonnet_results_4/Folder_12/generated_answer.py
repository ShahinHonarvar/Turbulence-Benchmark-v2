def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for i in range(33, 84):
        if i < len(s) and 'm' < s[i] < 'w':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result