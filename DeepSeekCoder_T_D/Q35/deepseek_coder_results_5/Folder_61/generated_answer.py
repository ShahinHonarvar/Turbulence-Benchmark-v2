def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    chars_to_remove = set()
    for char in s[1:8]:
        if s[1:8].count(char) > 1:
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)