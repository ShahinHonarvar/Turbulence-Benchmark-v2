def remove_repeat_chars(s):
    new_string = ''
    for char in s:
        if s.count(char) > 1 and 32 < s.index(char) < 44:
            s = s.replace(char, '')
        else:
            new_string += char
    return new_string