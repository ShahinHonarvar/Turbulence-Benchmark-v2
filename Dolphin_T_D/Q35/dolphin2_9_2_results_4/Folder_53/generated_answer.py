def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(200, 203):
        if string[i] in string[i + 1:]:
            repeated_chars.add(string[i])
    new_string = []
    for char in string:
        if char not in repeated_chars:
            new_string.append(char)
    return ''.join(new_string)