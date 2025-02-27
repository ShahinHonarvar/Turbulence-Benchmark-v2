def filter_chars(s):
    chars_to_remove = set()
    for i in range(283, 484):
        if i < len(s) and 'l' < s[i] < 't':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)