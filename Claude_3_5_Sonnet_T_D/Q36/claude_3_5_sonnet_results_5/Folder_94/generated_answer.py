def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for i in range(15, 85):
        if i < len(s) and 'I' < s[i] < 'M':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result