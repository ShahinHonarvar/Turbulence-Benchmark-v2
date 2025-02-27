def remove_repeat_chars(s):
    if len(s) < 7:
        return s
    to_remove = set()
    for char in s[1:6]:
        if s[1:6].count(char) > 1:
            to_remove.add(char)
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)