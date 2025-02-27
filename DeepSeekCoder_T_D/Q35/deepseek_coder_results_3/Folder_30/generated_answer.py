def remove_repeat_chars(s):
    to_remove = set()
    for i in range(22, 24):
        if s[i] in s[:i] + s[i + 1:] and s[i] not in to_remove:
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)