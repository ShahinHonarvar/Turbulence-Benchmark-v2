def remove_repeat_chars(str):
    str = str[:69] + ''.join(sorted(set(str[69:97]))) + str[97:]
    return str