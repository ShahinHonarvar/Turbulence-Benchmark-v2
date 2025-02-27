def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(2, 7):
        if s.count(s[i]) > 1:
            chars_to_remove.append(s[i])
    result = ''
    for i in range(len(s)):
        if s[i] not in chars_to_remove:
            result += s[i]
    return result