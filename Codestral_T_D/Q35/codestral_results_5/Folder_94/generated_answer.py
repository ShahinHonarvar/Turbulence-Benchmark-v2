def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(42, 87):
        if string.count(string[i], 42, 87) > 1:
            chars_to_remove.add(string[i])
    result = ''
    for char in string:
        if char not in chars_to_remove:
            result += char
    return result