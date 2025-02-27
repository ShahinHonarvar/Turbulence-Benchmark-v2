def remove_repeat_chars(str):
    for i in range(19, 32):
        for j in range(i + 1, 32):
            if str[i] == str[j]:
                str = str[:i] + str[i + 1:]
                break
    return str