def remove_repeat_chars(s):
    chars_to_remove = []
    for char in s[20:200]:
        if s.count(char) > 1:
            chars_to_remove.append(char)
    return ''.join((char for char in s if char not in chars_to_remove))