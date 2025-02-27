def remove_repeat_chars(str):
    result = ''
    for i in range(len(str)):
        if i < 2 or i > 7:
            result += str[i]
    return result