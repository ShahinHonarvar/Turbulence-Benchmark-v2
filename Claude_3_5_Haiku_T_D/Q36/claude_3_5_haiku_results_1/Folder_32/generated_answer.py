def filter_chars(s):
    if len(s) <= 41:
        return s
    chars_to_remove = set()
    for i in range(41, 63):
        if '7' < s[i] < 'H':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)