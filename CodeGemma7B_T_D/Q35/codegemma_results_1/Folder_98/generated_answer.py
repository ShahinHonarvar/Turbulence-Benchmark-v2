def remove_repeat_chars(str):
    for ind in range(8):
        for i in range(ind + 1, len(str)):
            if str[i] == str[ind]:
                str = str[:i] + str[i + 1:]
    return str