def remove_repeat_chars(str):
    str = list(str)
    for i in range(len(str)):
        if 0 < i < 5 and str[i] in str[i + 1:]:
            str[i] = ''
    str = ''.join(str)
    return str