def filter_chars(s):
    chars_to_remove = []
    for i in range(155, 404):
        if i < len(s) and '(' <= s[i] <= ']':
            chars_to_remove.append(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)