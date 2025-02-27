def remove_repeat_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 44 or i > 67:
            result += string[i]
    return result