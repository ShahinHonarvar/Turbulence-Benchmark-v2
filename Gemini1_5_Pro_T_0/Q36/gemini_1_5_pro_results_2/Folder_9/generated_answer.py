def filter_chars(s):
    chars_to_remove = set()
    for i in range(51, 91):
        if s[i] > 'A' and s[i] < 'Q':
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)