def filter_chars(s):
    result = []
    to_remove = set()
    for i in range(172, 636):
        if i < len(s) and 'c' < s[i] < 's':
            to_remove.add(s[i])
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)