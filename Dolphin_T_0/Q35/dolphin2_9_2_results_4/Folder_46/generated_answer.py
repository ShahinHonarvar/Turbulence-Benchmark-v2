def remove_repeat_chars(string):
    to_remove = set()
    for char in string[10:79]:
        if string.count(char) > 1:
            to_remove.add(char)
    result = ''.join([char for char in string if char not in to_remove])
    return result