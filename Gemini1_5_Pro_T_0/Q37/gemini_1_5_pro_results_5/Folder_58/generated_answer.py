def filter_chars(s):
    chars_to_remove = set()
    for i in range(503, 754):
        if i < len(s) and '9' <= s[i] <= 'w':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)