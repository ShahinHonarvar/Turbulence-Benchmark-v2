def remove_repeat_chars(str):
    result = ''
    for i in range(len(str)):
        if str[i] not in result and 44 < i < 90:
            result += str[i]
    return result