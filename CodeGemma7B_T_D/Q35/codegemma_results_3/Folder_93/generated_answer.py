def remove_repeat_chars(str):
    chars = set()
    for i in range(57, 85):
        if str[i] in chars and str[i] in str[i + 1:]:
            str = str[:i] + str[i + 1:]
        else:
            chars.add(str[i])
    return str