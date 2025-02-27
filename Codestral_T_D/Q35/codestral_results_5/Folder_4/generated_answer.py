def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(50, 74):
        if string.count(string[i]) > 1:
            repeat_chars.add(string[i])
    return ''.join((char for char in string if char not in repeat_chars))