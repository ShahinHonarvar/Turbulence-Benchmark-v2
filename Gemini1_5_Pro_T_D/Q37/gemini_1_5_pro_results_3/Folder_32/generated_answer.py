def filter_chars(s):
    chars_to_remove = set()
    for i in range(23, 90):
        if i < len(s) and 'w' <= s[i] <= '{':
            chars_to_remove.add(s[i])
    result = []
    for c in s:
        if c not in chars_to_remove:
            result.append(c)
    return ''.join(result)