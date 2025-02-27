def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(13, 70):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    result = ''
    for i in range(len(s)):
        if s[i] not in chars_to_remove:
            result += s[i]
    return result