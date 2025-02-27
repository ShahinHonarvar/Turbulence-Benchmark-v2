def remove_repeat_chars(s):
    start, end = (6, 9)
    chars_to_remove = set()
    for i in range(start + 1, end):
        if s[start:end].count(s[i]) > 1:
            chars_to_remove.add(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)