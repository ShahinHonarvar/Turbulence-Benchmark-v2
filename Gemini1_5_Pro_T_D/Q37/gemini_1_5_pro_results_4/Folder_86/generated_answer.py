def filter_chars(s):
    chars_to_remove = set()
    for i in range(164, 707):
        if i < len(s) and 'O' <= s[i] <= '}':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)