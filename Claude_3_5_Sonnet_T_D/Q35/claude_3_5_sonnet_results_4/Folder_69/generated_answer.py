def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in s[40:43]:
        if s[40:43].count(char) > 1:
            chars_to_remove.add(char)
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result