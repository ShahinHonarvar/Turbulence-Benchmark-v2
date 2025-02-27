def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(10, 100):
        if s[i] in s[:i] + s[i + 1:]:
            chars_to_remove.add(s[i])
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result