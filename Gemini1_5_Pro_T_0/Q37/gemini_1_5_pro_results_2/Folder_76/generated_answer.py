def filter_chars(s):
    chars_to_remove = set()
    for i in range(379, 899):
        if i < len(s) and 'M' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)