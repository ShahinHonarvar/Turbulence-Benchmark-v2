def remove_repeat_chars(s):
    result = ''
    for index, char in enumerate(s):
        if 20 < index < 200 and s.count(char) > 1:
            result += char
    return result