def remove_repeat_chars(string):
    repeat_chars = {}
    new_string = ''
    for char in string:
        if 73 <= repeat_chars.get(char, -1) < 84 and (repeat_chars.get(char) != -1 or (string.index(char) > repeat_chars.get(char) and string.rindex(char) < 84)):
            new_string += string.replace(char, '')
        else:
            repeat_chars[char] = string.rindex(char)
    return new_string