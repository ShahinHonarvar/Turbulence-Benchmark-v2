def remove_repeat_chars(str):
    temp = str[72:93]
    seen_chars = set()
    new_str = ''
    for char in temp:
        if char not in seen_chars:
            seen_chars.add(char)
            new_str += char
    str = str[:72] + new_str + str[93:]
    return str