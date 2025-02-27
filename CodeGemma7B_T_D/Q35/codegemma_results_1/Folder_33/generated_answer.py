def remove_repeat_chars(str):
    for i in range(125, 825):
        for c in str[i]:
            if str[i].count(c) > 1:
                str[i] = str[i].replace(c, '')
    return str