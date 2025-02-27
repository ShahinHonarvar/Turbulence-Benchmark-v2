def remove_repeat_chars(s):
    sub_string = s[62:96]
    chars_to_remove = []
    for char in sub_string:
        if sub_string.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.append(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result