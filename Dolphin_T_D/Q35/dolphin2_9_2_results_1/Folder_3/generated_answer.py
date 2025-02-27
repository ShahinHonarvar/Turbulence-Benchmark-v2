def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(56, 88):
        if s[i] in s[i + 1:88]:
            chars_to_remove.add(s[i])
    result = ''
    for i in range(len(s)):
        if s[i] not in chars_to_remove:
            result += s[i]
    return result