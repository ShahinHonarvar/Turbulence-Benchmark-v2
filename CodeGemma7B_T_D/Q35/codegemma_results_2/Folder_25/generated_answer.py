def remove_repeat_chars(str):
    new_str = str[0:37] + ''.join((char for char in str[37:43] if char not in str[37:43][str[37:43].index(char):])) + str[43:]
    return new_str