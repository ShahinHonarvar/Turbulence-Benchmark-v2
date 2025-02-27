def remove_repeat_chars(str):
    str = str[:12] + ''.join(list(filter(lambda x: x not in str[13:77] or str[13:77].count(x) <= 1, str[13:77]))) + str[77:]
    return str