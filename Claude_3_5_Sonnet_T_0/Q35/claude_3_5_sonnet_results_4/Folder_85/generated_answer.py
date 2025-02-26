def remove_repeat_chars(s):
    chars_to_remove = set()
    for char in s[1:8]:
        if s[1:8].count(char) > 1:
            chars_to_remove.add(char)
    result = s[0]
    for char in s[1:]:
        if char not in chars_to_remove:
            result += char
    return result