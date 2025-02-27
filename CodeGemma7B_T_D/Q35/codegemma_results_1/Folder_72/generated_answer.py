def remove_repeat_chars(str):
    counts = {}
    for i in range(13, 70):
        if str[i] in counts:
            str = str.replace(str[i], '')
        else:
            counts[str[i]] = 1
    return str