def remove_repeat_chars(str):
    result = ''
    b = 56
    _a = 90
    while b < _a:
        char = str[b]
        if result.find(char) == -1:
            result += char
        b += 1
    return result