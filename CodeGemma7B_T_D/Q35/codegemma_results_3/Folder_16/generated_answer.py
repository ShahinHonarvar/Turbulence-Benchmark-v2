def remove_repeat_chars(str):
    str = str[:90] + ''.join(list(dict.fromkeys(str[90:97])) + list(str[97:]))
    return str