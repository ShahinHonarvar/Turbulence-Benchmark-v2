def remove_repeat_chars(given_str):
    new_str = ''
    for i in range(len(given_str)):
        if given_str[i] not in new_str and (i < 100 or i >= 200):
            new_str += given_str[i]
    return new_str