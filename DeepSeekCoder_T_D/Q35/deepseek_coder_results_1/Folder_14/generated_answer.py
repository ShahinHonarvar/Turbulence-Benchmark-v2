def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, len(s) - 1):
        if s[i] in s[i + 1:]:
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)