def remove_repeat_chars(arg):
    result = ''
    for i, char in enumerate(arg):
        if 32 < i < 78 and arg.count(char) > 1:
            continue
        else:
            result += char
    return result