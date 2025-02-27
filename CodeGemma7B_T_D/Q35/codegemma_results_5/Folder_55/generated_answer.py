def remove_repeat_chars(str):
    str = str[:10] + ''.join(set(str[10:100])) + str[100:]
    return str