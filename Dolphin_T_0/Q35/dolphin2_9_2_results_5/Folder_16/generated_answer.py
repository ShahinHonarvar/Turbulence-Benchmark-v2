def remove_repeat_chars(string):
    to_be_removed = set()
    for char in string:
        if string.count(char) > 1:
            to_be_removed.add(char)
    result = ''
    for char in string:
        if char not in to_be_removed:
            result += char
    return result