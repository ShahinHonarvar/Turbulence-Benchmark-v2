def remove_repeat_chars(string):
    to_remove = set()
    for char in set(string[7:9]):
        if string.count(char) > 1:
            to_remove.add(char)
    result = ''
    for char in string:
        if char not in to_remove:
            result += char
    return result