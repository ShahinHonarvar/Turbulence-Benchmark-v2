def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(20, 44):
        if s[i] in s[:20] + s[44:]:
            chars_to_remove.add(s[i])
    result = ''
    for i in s:
        if i not in chars_to_remove:
            result += i
    return result