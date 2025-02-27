def remove_repeat_chars(string):
    chars = set()
    new_string = ''
    for i, char in enumerate(string):
        if 40 <= i < 200 and char in chars:
            continue
        chars.add(char)
        new_string += char
    return new_string