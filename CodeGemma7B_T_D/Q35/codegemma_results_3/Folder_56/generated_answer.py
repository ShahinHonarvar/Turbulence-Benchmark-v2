def remove_repeat_chars(str):
    str = list(str)
    for i in range(7, 9):
        while i + 1 < len(str) and str[i] == str[i + 1]:
            str.remove(str[i])
    return ''.join(str)